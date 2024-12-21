from PyQt5 import QtWidgets,QtCore



class Ui_Mainwindow(object):

    def UIcomponents(self):

        MainWindow.resize(800, 600)
        c = QtWidgets.QWidget(MainWindow)
        c.setObjectName("c")
        c.resize(800, 600)



    def setup(self):


        gamer=QtWidgets.QPushButton()
        gamer.setGeometry(QtCore.QRect(10,10,100,50))
        gamer.settext("gamer:")
        gamer.clicked.connect(self.gamer)

        start = QtWidgets.QPushButton()
        start.setGeometry(QtCore.QRect(500, 100, 100, 50))
        start.setText("start!")
        start.clicked.connect(self.start)


        save = QtWidgets.QPushButton()
        save.setGeometry(QtCore.QRect(500, 200, 100, 50))
        save.setText("save")
        save.clicked.connect(self.savegame)


        exit = QtWidgets.QPushButton()
        exit.setGeometry(QtCore.QRect(500, 300, 100, 50))
        exit.setText("exit")
        exit.clicked.connect(self.exit)


    def startgame(self):
        print("start!")

    def gamer(self):
        print("gamer")

    def savegame(self):
        print("save!")

    def exit(self):
        print("exit!")




if __name__ =="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    Ui_Mainwindow.setup(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())