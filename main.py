from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow #QApplication,QWidget
from PyQt5.QtCore import *
#from PyQt5.QtGui import QPainter, QColor
import fonction



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window=fonction.Mainwindow()
    window.show()
    sys.exit(app.exec_())










