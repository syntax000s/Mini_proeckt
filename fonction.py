from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import random


class SnakeGame(QWidget):
    def __init__(self):
        super().__init__()
        self.square_size = 20
        self.snake = [(10, 10)]
        self.direction = 'RIGHT'

        self.food = self.generate_food()
        self.initUI()

    def initUI(self):
        self.setGeometry(100,100,500, 500)
        self.setWindowTitle('Snake Game')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_snake(qp)
        self.draw_food(qp)
        qp.end()

    def draw_snake(self, qp):
        for x, y in self.snake:
            qp.fillRect(x * self.square_size, y * self.square_size, self.square_size, self.square_size,
                        QColor(0, 255, 0))

    def draw_food(self, qp):
        x, y = self.food
        qp.fillRect(x * self.square_size, y * self.square_size, self.square_size, self.square_size, QColor(255, 0, 0))

    def generate_food(self):
        x = random.randint(0, 24)
        y = random.randint(0, 24)
        return (x, y)

    def keyPressEvent(self, e):
        if Qt.Key() == Qt.Key.Key_Up:
            print("up")
            self.direction = 'UP'
        if Qt.Key().Key_Down == Qt.Key().Key_Down:
            print("down")
            self.direction = 'DOWN'
        if Qt.Key.Key_Left == Qt.Key.Key_Left:
            print("Left")
            self.direction = 'LEFT'
        if Qt.Key.Key_Right == Qt.Key.Key_Right:
            print("Right")
            self.direction = 'RIGHT'
        self.e.accept()

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("myGame")

        self.setGeometry(100,100,600, 450)
        self.dialog=SnakeGame()
        self.UIcomponents()

    def UIcomponents(self):

        gamer = QtWidgets.QPushButton("a", self)
        gamer.setGeometry(10,10,100,50)
        gamer.setText("gamer:")
        gamer.clicked.connect(self.gamer)

        start =QtWidgets.QPushButton("b",self)
        start.setGeometry(500, 100, 100, 50)
        start.setText("start!")
        start.clicked.connect(self.startgame)


        save = QtWidgets.QPushButton("c", self)
        save.setGeometry(500, 200, 100, 50)
        save.setText("save")
        save.clicked.connect(self.savegame)


        off =QtWidgets.QPushButton("d", self)
        off.setGeometry(500, 300, 100, 50)
        off.setText("exit")
        off.clicked.connect(self.off)

    def startgame(self):
        print("start!")
        self.dialog.show()

    def gamer(self):
        print("gamer")

    def savegame(self):
        print("save!")

    def off(self):
        print("exit!")
        self.close()










