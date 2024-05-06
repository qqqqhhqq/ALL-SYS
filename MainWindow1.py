# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(2026, 1213)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 60, 1561, 651))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imgView = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.imgView.setStyleSheet("border: 1px solid black;background-color: #E0E0E0;")
        self.imgView.setText("")
        self.imgView.setObjectName("imgView")
        self.horizontalLayout.addWidget(self.imgView)
        self.graphView = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.graphView.setStyleSheet("border: 1px solid black;background-color: #E0E0E0;")
        self.graphView.setText("")
        self.graphView.setObjectName("graphView")
        self.horizontalLayout.addWidget(self.graphView)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(900, 770, 861, 381))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.action_info = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.action_info.setStyleSheet("background:#FFFFFF")
        self.action_info.setText("")
        self.action_info.setObjectName("action_info")
        self.action_info.setWordWrap(True)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.action_info.setFont(font)
        self.horizontalLayout_2.addWidget(self.action_info)
        self.ctroller = QtWidgets.QWidget(self.centralwidget)
        self.ctroller.setGeometry(QtCore.QRect(90, 820, 851, 351))
        self.ctroller.setObjectName("ctroller")
        self.import_2 = QtWidgets.QPushButton(self.ctroller)
        self.import_2.setGeometry(QtCore.QRect(170, 30, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.import_2.setFont(font)
        self.import_2.setObjectName("import_2")
        self.load_model = QtWidgets.QPushButton(self.ctroller)
        self.load_model.setGeometry(QtCore.QRect(490, 30, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.load_model.setFont(font)
        self.load_model.setObjectName("load_model")
        self.generate = QtWidgets.QPushButton(self.ctroller)
        self.generate.setGeometry(QtCore.QRect(330, 140, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.generate.setFont(font)
        self.generate.setObjectName("generate")
        self.detect = QtWidgets.QPushButton(self.ctroller)
        self.detect.setGeometry(QtCore.QRect(50, 140, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.detect.setFont(font)
        self.detect.setObjectName("detect")
        self.export_2 = QtWidgets.QPushButton(self.ctroller)
        self.export_2.setGeometry(QtCore.QRect(160, 260, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.export_2.setFont(font)
        self.export_2.setObjectName("export_2")
        self.close = QtWidgets.QPushButton(self.ctroller)
        self.close.setGeometry(QtCore.QRect(490, 260, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.close.setFont(font)
        self.close.setObjectName("close")
        self.understand = QtWidgets.QPushButton(self.ctroller)
        self.understand.setGeometry(QtCore.QRect(590, 140, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.understand.setFont(font)
        self.understand.setObjectName("understand")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 0, 721, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.video_ctr = QtWidgets.QWidget(self.centralwidget)
        self.video_ctr.setGeometry(QtCore.QRect(80, 730, 771, 80))
        self.video_ctr.setObjectName("video_ctr")
        self.progress = QtWidgets.QSlider(self.video_ctr)
        self.progress.setGeometry(QtCore.QRect(30, 10, 851, 22))
        self.progress.setOrientation(QtCore.Qt.Horizontal)
        self.progress.setObjectName("progress")
        self.suspend = QtWidgets.QPushButton(self.video_ctr)
        self.suspend.setGeometry(QtCore.QRect(320, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.suspend.setFont(font)
        self.suspend.setObjectName("suspend")
        self.play = QtWidgets.QPushButton(self.video_ctr)
        self.play.setGeometry(QtCore.QRect(440, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.play.setFont(font)
        self.play.setObjectName("play")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1680, 20, 321, 691))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listView_obj = QtWidgets.QListView(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listView_obj.setFont(font)
        self.listView_obj.setObjectName("listView_obj")
        self.verticalLayout.addWidget(self.listView_obj)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listView_rel = QtWidgets.QListView(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listView_rel.setFont(font)
        self.listView_rel.setObjectName("listView_rel")
        self.verticalLayout.addWidget(self.listView_rel)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1270, 730, 151, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.import_2.setText(_translate("MainWindow", "导入"))
        self.load_model.setText(_translate("MainWindow", "加载模型"))
        self.generate.setText(_translate("MainWindow", "场景图生成"))
        self.detect.setText(_translate("MainWindow", "目标检测"))
        self.export_2.setText(_translate("MainWindow", "导出"))
        self.close.setText(_translate("MainWindow", "关闭"))
        self.understand.setText(_translate("MainWindow", "行为理解"))
        self.label_3.setText(_translate("MainWindow", "基于海上场景图生成的目标行为理解演示系统"))
        self.suspend.setText(_translate("MainWindow", "⏸"))
        self.play.setText(_translate("MainWindow", "▶"))
        self.label_2.setText(_translate("MainWindow", "目标信息"))
        self.label.setText(_translate("MainWindow", "关系信息"))
        self.label_6.setText(_translate("MainWindow", "行为理解信息"))