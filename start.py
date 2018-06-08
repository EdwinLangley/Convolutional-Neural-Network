import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStyleFactory

class Mainwindow():

    def __init__(self):
        self.dlg = uic.loadUi("GUI.ui")
        self.dlg.run_cat.clicked.connect(self.hello)
        self.dlg.show()

    def hello(self):
        print("hello")



if __name__ == "__main__":
    app = QApplication([])
    app.setStyle(QStyleFactory.create('Fusion'))
    form = Mainwindow()
    app.exec()