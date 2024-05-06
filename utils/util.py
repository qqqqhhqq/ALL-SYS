import cv2
import numpy as np
from PyQt5.QtGui import QPixmap, QImage ,QColor


# def qtpixmap_to_cvimg(qtpixmap):
#     qimg = qtpixmap.toImage()
#     temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
#     temp_shape += (4,)
#     ptr = qimg.bits()
#     ptr.setsize(qimg.byteCount())
#     result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
#     result = result[..., :3]
#     return result
def xywh_to_xyxy(bbox_xywh):
    x, y, w, h = bbox_xywh
    x1 = x
    y1 = y
    x2 = x + w
    y2 = y + h
    return x1, y1, x2, y2



def qpixmap_to_opencv(qpixmap):
    # Convert QPixmap to QImage
    qimage = qpixmap.toImage()

    # Ensure the image is in the RGB format
    qimage = qimage.convertToFormat(QImage.Format_ARGB32)

    # Get image size
    width = qimage.width()
    height = qimage.height()

    # Create buffer
    buffer = np.empty((height, width, 4), dtype=np.uint8)

    # Copy image data into buffer
    for y in range(height):
        for x in range(width):
            color = QColor(qimage.pixel(x, y))
            buffer[y, x, 0] = color.red()
            buffer[y, x, 1] = color.green()
            buffer[y, x, 2] = color.blue()
            buffer[y, x, 3] = color.alpha()

    # Convert image format (ARGB to BGR)
    cv_image = cv2.cvtColor(buffer, cv2.COLOR_RGBA2BGR)

    return cv_image

def opencv_to_qimage(cv_image):
    # Convert image format (BGR to RGB)
    rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

    # Create QImage from numpy array
    height, width, channels = rgb_image.shape
    bytes_per_line = channels * width
    qimage = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

    return qimage

def draw_bounding_boxes(qpixmap, bboxes, labels, color=(0, 255, 0), thickness=2):
    # 将 QPixmap 转换为 OpenCV 格式的图像
    cv_image = qpixmap_to_opencv(qpixmap)
    # 绘制每个边界框和标签
    for bbox, label in zip(bboxes, labels):
        x1, y1, x2, y2 = bbox
        # 绘制边界框
        cv2.rectangle(cv_image, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)
        # 添加标签信息
        cv2.putText(cv_image, label, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, thickness)
        # 将 OpenCV 格式的图像转换回 QPixmap
    qimage = opencv_to_qimage(cv_image)
    updated_qpixmap = QPixmap.fromImage(qimage)
    return updated_qpixmap