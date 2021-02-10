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
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 900, 600)
        self.zero = (self.width()//2, self.height()//2)
        self.delay = 40
        self.total_rot = 0
        self.setWindowTitle('Matrix')
        self.createShape()
        self.show()

    def createShape(self):
        self.shape = [
            [50, 50, 1],
            [20, 80, 1],
            [-40, 80, 1],
            [-70, 120, 1],
            [-10, 120, 1],
            [20, 80, 1]
        ]
        self.rotate(10)

    def transform(self):
        phi=4
        self.total_rot = (self.total_rot+phi)%360
        print(self.total_rot)
        if math.cos(self.total_rot * math.pi / 180) > 0.0:
            self.rotate(phi*abs(math.cos(self.total_rot * math.pi / 180))**2)    # Looks complicated, gravity pretend
        elif math.cos(self.total_rot * math.pi / 180) < -0.0:
            self.rotate(phi*abs(math.cos(self.total_rot * math.pi / 180))**2 * -1)
        self.transfer(0, 1)
        self.resize(1.002, 1.002)
        self.update()


    def rotate(self, degrees):
        phi = degrees * math.pi / 180
        rot = np.array([
            [math.cos(phi),      math.sin(phi), 0],
            [-1 * math.sin(phi), math.cos(phi), 0],
            [0,                  0,             1]
        ])
        for i in range(len(self.shape)):
            self.shape[i] = np.array(self.shape[i]).dot(rot)

    def transfer(self, x, y):
        move = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [x, y, 1],
        ])
        for i in range(len(self.shape)):
            self.shape[i] = np.array(self.shape[i]).dot(move)

    def resize(self, a, b):
        scale = np.array([
            [a, 0, 0],
            [0, b, 0],
            [0, 0, 1],
        ])
        for i in range(len(self.shape)):
            self.shape[i] = np.array(self.shape[i]).dot(scale)


    def paintEvent(self, event):
        width = self.size().width()
        height = self.size().height()
        painter = QPainter(self)
        pen = QPen(Qt.black)
        pen.setWidth(4)
        painter.setPen(pen)

        #painter.drawLine(self.zero[0],0,self.zero[0],self.height())

        self.drawShape(painter)

    def drawShape(self, painter):
        for i in range(len(self.shape)-1):
            painter.drawLine(self.shape[i][0]+self.zero[0],
                             self.shape[i][1],
                             self.shape[i+1][0] + self.zero[0],
                             self.shape[i + 1][1]
                             )
        self.timer.start(self.delay)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = AnimAlgos()
    w.show()
    sys.exit(app.exec_())
