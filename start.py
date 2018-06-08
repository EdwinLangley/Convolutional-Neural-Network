# import sys
# from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStyleFactory
# from PyQt5.QtCore import pyqtSlot
# from tabs import Ui_MainWindow
#
# # class AppWindow(QDialog):
# #     def __init__(self):
# #         super().__init__()
# #         self.ui = Ui_MainWindow()
# #         self.ui.setupUi(self)
# #         print("hi")
# #         self.show()
# #
# #     @pyqtSlot()
# #     def on_pushButton_clicked(self):
# #         print("hi")
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setStyle(QStyleFactory.create('Fusion'))
#     ex = Ui_MainWindow()
#     w = QMainWindow()
#     ex.setupUi(w)
#     w.show()
#     sys.exit(app.exec_())
#
#     app.run_cat.clicked.connect(hello)
#
# def hello():
#     print("Hello")

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStyleFactory
from tabs import Ui_MainWindow

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