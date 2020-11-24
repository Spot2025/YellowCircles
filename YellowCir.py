import sys

from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.run)


    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.qp.setPen(QColor(0, 0, 0))
            self.qp.setBrush(QColor(255, 255, 0))
            self.draw()
            self.qp.end()

    def draw(self):
        size = randint(1, 100)
        coords = (randint(0, 600 - size), randint(0, 600 - size))
        self.qp.drawEllipse(*coords, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
