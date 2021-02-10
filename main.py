from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from math import sqrt
import time

class DrawAlgos(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Matrix')
        self.show()


    def paintEvent(self, event):
        width = self.size().width()
        height = self.size().height()
        painter = QPainter(self)
        pen = QPen(Qt.black)
        painter.setPen(pen)

        #painter.drawPoint(x, y)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = DrawAlgos()
    w.show()
    sys.exit(app.exec_())
