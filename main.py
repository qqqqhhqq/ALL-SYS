import pickle
import sys
import os
import PyQt5.QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QMessageBox
from PyQt5.QtCore import Qt, QUrl, QTimer , QStringListModel
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QGraphicsVideoItem
from MainWindow1 import Ui_MainWindow
from utils.util import *
import cv2
import json

import networkx as nx
import matplotlib.pyplot as plt

base_path =  os.getcwd()

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Main Window")
        self.setFixedSize(2010, 1213)
        self.meta_cache = "meta_cache.pickle"
        self.meta_folder = os.path.join(base_path, "meta")
        self.cur_img = None
        self.image_name = None
        self.model = None
        self.image_data = None
        self.objects_data = None
        self.relationships_data = None
        self.labels = None
        self.objs = None
        self.triples = None


        #-------------------------
        self.isDetect = False
        self.isSGG = False

        #--------------------------

        self.init_app()
        self.connect()

    def get_imid_by_name(self, filename):
        return self.image_data.index(filename)

    def connect(self):
        self.ui.import_2.clicked.connect(self.import_data)
        self.ui.load_model.clicked.connect(self.load_model)
        self.ui.detect.clicked.connect(self.detect)
        self.ui.generate.clicked.connect(self.generate)
        self.ui.export_2.clicked.connect(self.export)
        self.ui.close.clicked.connect(self.close)
        self.ui.understand.clicked.connect(self.understand)


    def understand(self):
        self.ui.action_info.setText("usv are collaborate to each other to protect an important cargo in front of the island")


    def close(self):
        reply = QMessageBox.question(self , "退出", "你要退出程序吗?" , QMessageBox.Yes | QMessageBox.No , QMessageBox.No)
        if reply == QMessageBox.Yes:
            QApplication.quit()

    def export(self):

        if self.objs is None:
            QMessageBox.critical(self , "警告" ,"没有目标信息" , QMessageBox.Ok)
            return

        if self.triples is None:
            QMessageBox.critical(self , "警告" ,"没有关系信息" , QMessageBox.Ok)
            return

        obj_data = []
        for l , b in self.objs:
            e = {
                'name': l,
                'x' : b[0],
                'y' : b[1],
                'w' : b[2] - b[0],
                'h' : b[3] - b[1]
            }
            obj_data.append(e)

        rel_data = []
        for tri in self.triples:
            r = {
                'sub': tri[0],
                'predicate' : tri[1],
                'obj' : tri[2]
            }
            rel_data.append(r)

        data = {'objects' : obj_data , 'relationships' : rel_data}
        out_file = os.path.join(os.getcwd() , os.path.splitext(self.image_name)[0] + '.json')

        if os.path.exists(out_file):
            with open(out_file, 'w') as file:
                json.dump(data , file)
        else:
            with open(out_file , 'w') as file:
                json.dump(data , file)

        QMessageBox.information(self , "通知" , "图片信息已经到处" , QMessageBox.Ok)

    def generate(self):
        if self.image_name is None:
            QMessageBox.critical(self, "失败", "没有导入图片")
            return

        if not self.isDetect :
            QMessageBox.critical(self, "失败", "请先进行目标检测")
            return

        im_id = self.get_imid_by_name(self.image_name)
        self.triples = self.get_rel_info_by_id(im_id)
        triples_model = ['<' + triple[0]  + ',' + triple[1] + ',' + triple[2] + '>' for triple in self.triples ]

        self.draw_scene_graph(self.triples , self.labels)
        modelView = QStringListModel()
        modelView.setStringList(triples_model)
        self.ui.listView_rel.setModel(modelView)

    def draw_scene_graph(self , triples , labels):
        netxG = nx.DiGraph()
        relationships = []

        for l in labels:
            netxG.add_node(l)

        for triple in triples:
            netxG.add_edge(triple[0], triple[2], relation=triple[1])

        graphview_width = self.ui.graphView.width()
        graphview_height = self.ui.graphView.height()

        # 绘制图像
        plt.figure(figsize=(  graphview_width/ 100,   graphview_height / 100))  # 设置图的大小为 QLabel 的大小
        pos = nx.planar_layout(netxG) # 指定图的布局
        nx.draw(netxG, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=14, ax=plt.gca())  # 绘制节点

        plt.tight_layout()
        # 绘制带有关系属性的边
        edge_labels = nx.get_edge_attributes(netxG, 'relation')
        for edge, label in edge_labels.items():
            x = pos[edge[0]][0]  # 起点 x 坐标
            y = pos[edge[0]][1]  # 起点 y 坐标
            x_end = pos[edge[1]][0]  # 终点 x 坐标
            y_end = pos[edge[1]][1]  # 终点 y 坐标
            # 计算标签位置（取两点连线的中点）
            label_x = (x + x_end) / 2
            label_y = (y + y_end) / 2
            # 截断或调整标签文本
            if len(label) > 10:  # 如果标签长度超过10，截断
                label = label[:10] + "..."
            plt.text(label_x, label_y, label, horizontalalignment='center', verticalalignment='center', fontsize=12)

        canvas = plt.gcf().canvas
        canvas.draw()
        print(graphview_height)
        img = QImage(canvas.buffer_rgba(), graphview_width, graphview_height, QImage.Format_RGBA8888)

        pixmap = QPixmap.fromImage(img)
        self.ui.graphView.setPixmap(pixmap)
        plt.close()


    def get_rel_info_by_id(self, id):
        assert id < len(self.relationships_data)
        return  self.relationships_data[id]

    def detect(self):
        if self.model is None:
            QMessageBox.critical(self , "失败" , "模型没有加载")
            return
        if self.image_name is None:
            QMessageBox.critical(self, "失败", "没有导入图片")
            return

        im_id = self.get_imid_by_name(self.image_name)
        bboxes , labels =  self.get_obj_info_by_id(im_id)
        self.objs = [(label , bboxe)  for label , bboxe in zip( labels, bboxes)]
        self.labels = labels
        update_opixmap = draw_bounding_boxes(self.cur_img , bboxes , labels , color=(0 , 255, 0) , thickness=2)
        update_opixmap = update_opixmap.scaled(self.ui.imgView.size(), Qt.KeepAspectRatio)

        self.ui.imgView.setPixmap(update_opixmap)
        listModel = QStringListModel()
        listModel.setStringList(labels)
        self.ui.listView_obj.setModel(listModel)
        self.isDetect = True

    def get_obj_info_by_id(self, id):
        assert  id < len(self.objects_data)

        objs = self.objects_data[id]

        bboxes = []
        labels = []
        for obj in objs:
            labels.append(obj[0])
            bbox_xywh = obj[1][0],obj[1][1],obj[1][2],obj[1][3]
            bbox_xyxy = xywh_to_xyxy(bbox_xywh)
            bboxes.append(bbox_xyxy)
        return bboxes , labels

    def load_model(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "选择模型文件", "", "YAML Files (*.yaml)", options=options)
        if filename:
            # 加载模型的代码可以在这里添加
            status = f"模型已加载：{filename}"
            QMessageBox.warning(self, "通知" , "模型加载成功" ,QMessageBox.Ok)
            self.model = filename
            self.statusBar().showMessage(status)
            # print(status)
        else:
            QMessageBox.warning(self, "警告", "没有选择模型配置文件！", QMessageBox.Ok)

    def import_data(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, '选择文件', '.', 'Images (*.png *.jpg *.bmp)')

        if self.file_path:
            try:
                if self.file_path.endswith(('.png', '.jpg', '.bmp')):
                    pixmap = QPixmap(self.file_path)
                    print(pixmap.width())
                    print(pixmap.height())
                    self.cur_img = pixmap
                    pixmap = pixmap.scaled(self.ui.imgView.size(), Qt.KeepAspectRatio)
                    self.ui.imgView.setPixmap(pixmap)
                    self.image_name = os.path.basename(self.file_path)

                    # ===============
                    model = QStringListModel()
                    model.setStringList([])
                    self.ui.listView_obj.setModel(model)
                    self.ui.listView_rel.setModel(model)
                    self.ui.graphView.clear()
                    # ===================
                elif self.file_path.endswith(('.mp4', '.avi', '.mov')):

                    QMessageBox.critical("请选择图片数据" ,QMessageBox.Warning)


            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def init_app(self):
        meta_data = self.load_meta_from_cache()
        if meta_data is not None:
            self.image_data = meta_data['image_data']
            self.objects_data = meta_data['objects_data']
            self.relationships_data = meta_data['relationship_data']
        else:
            self.image_data , self.objects_data, self.relationships_data = self.load_meta_from_files()
            meta_data = {
                "image_data" : self.image_data,
                "objects_data" : self.objects_data,
                "relationship_data" : self.relationships_data
            }
            self.save_meta_to_cache(meta_data)

    def load_meta_from_cache(self):
        if os.path.isfile(self.meta_cache):
            with open(self.meta_cache, "rb") as f:
                return pickle.load(f)
        else:
            return None

    def save_meta_to_cache(self, meta_data):
        with open(self.meta_cache, "wb") as f:
            pickle.dump(meta_data, f)

    def load_meta_from_files(self):
        image_data_path = os.path.join(self.meta_folder, "image_data.json")
        objects_path = os.path.join(self.meta_folder, "objects.json")
        relationships_path = os.path.join(self.meta_folder, "relationships.json")

        with open(image_data_path, "r") as f:
            image_data = json.load(f)
        with open(objects_path, "r") as f:
            objects_data = json.load(f)
        with open(relationships_path, "r") as f:
            relationships_data = json.load(f)

        image_data_list =[]
        for im in image_data:
            im_id = im['image_id']
            image_name = im['image_name']
            image_data_list.insert(im_id , image_name)

        obj_data_list = []
        for im_obj in objects_data:
            im_id = im_obj['image_id']
            objects = im_obj['objects']
            object_list = []
            for obj in objects:
                obj_name = obj['names'][0] + "-" + str(obj['object_id'])
                bbox = [obj['x'] , obj['y'] , obj['w'] , obj['h']]
                obj_info = (obj_name,  bbox)
                object_list.append(obj_info)
            obj_data_list.insert(im_id , object_list)


        rel_data_list = []
        for im_rel in relationships_data:
            im_id = im_rel['image_id']
            relations = im_rel['relationships']
            rel_list = []
            for rel in relations:
                sub_name = rel['subject']['name'] + '-' + str(rel['subject']['object_id'])
                obj_name = rel['object']['name'] + '-' + str(rel['object']['object_id'])
                predicate = rel['predicate']
                triple = (sub_name , predicate , obj_name)
                rel_list.append(triple)
            rel_data_list.insert(im_id , rel_list)

        return  image_data_list, obj_data_list, rel_data_list



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())
