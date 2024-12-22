
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter, QColor, QKeyEvent
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import random

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("myGame")
        self.setGeometry(100,100,600, 450)
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
        import snakegame

    def gamer(self):
        print("gamer")

    def savegame(self):
        print("save!")

    def off(self):
        print("exit!")
        self.close()









