
from PyQt5 import QtWidgets,QtCore


class Ui_Mainwindow(object):

    def setup(self):
        MainWindow.resize(800,600)
        self.c=QtWidgets.QWidget(MainWindow)
        self.c.setObjectName("c")
        self.c.resize(800,600)

        self.gamer=QtWidgets.QPushButton(self.c)
        self.gamer.setGeometry(QtCore.QRect(10,10,100,50))

        self.start = QtWidgets.QPushButton(self.c)
        self.start.setGeometry(QtCore.QRect(500, 100, 100, 50))

        self.nastr = QtWidgets.QPushButton(self.c)
        self.nastr.setGeometry(QtCore.QRect(500, 200, 100, 50))

        self.exit = QtWidgets.QPushButton(self.c)
        self.exit.setGeometry(QtCore.QRect(500, 300, 100, 50))


if __name__ =="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    Ui_Mainwindow.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())