from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
import numpy as np          # contains methods for comfortable matrix usage
import math

class AnimAlgos(QWidget):

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.transform)
        self.x = 50
        self.y = 50
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Matrix')
        self.show()

    def transform(self):
        phi = math.pi/90
        rot = np.aCrerray([
            [math.cos(phi), math.sin(phi)],
            [-1*math.sin(phi), math.cos(phi)]
        ])
        #self.x += 1
        #self.y += 1
        [self.x, self.y] = np.array([self.x, self.y]).dot(rot)
        self.update()

    def paintEvent(self, event):
        width = self.size().width()
        height = self.size().height()
        painter = QPainter(self)
        pen = QPen(Qt.black)
        pen.setWidth(10)
        painter.setPen(pen)

        painter.drawPoint(self.x+150, self.y+150)
        self.timer.start(5)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = AnimAlgos()
    w.show()
    sys.exit(app.exec_())
