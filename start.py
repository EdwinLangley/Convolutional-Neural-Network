import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStyleFactory, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QSize

class Mainwindow():

    def __init__(self):
        self.dlg = uic.loadUi("GUI.ui")
        self.dlg.run_cat.clicked.connect(self.run_category)
        self.dlg.open_target_btn.clicked.connect(self.open_image)
        self.dlg.save_output_btn.clicked.connect(self.save_output)
        self.dlg.run_train_btn.clicked.connect(self.run_train)
        self.dlg.imgaug_info_btn.clicked.connect(self.img_aug_dialog)
        self.dlg.passes_info_btn.clicked.connect(self.passes_dialog)
        self.dlg.show()

    def run_category(self):
        print("run_category: TODO")

    def open_image(self):
        """

        :return:
        """
        self.comparison_image, _ = QFileDialog.getOpenFileName(None, "Open Image", "~","Image Files (*.jpg *.png)")
        self.comparisonicon = QImage(self.comparison_image)
        self.comparisonscaledimage = self.comparisonicon.scaled(QSize(250, 250))
        self.dlg.selected_image.setPixmap(QPixmap.fromImage(self.comparisonscaledimage))
        self.dlg.target_img_src.setText(self.comparison_image)
        self.dlg.selected_image.show()

    def save_output(self):
        """

        :return:
        """
        print("save_output: TODO")

    def run_train(self):
        """

        :return:
        """
        print("run_train: TODO")

    def img_aug_dialog(self):
        """

        :return:
        """
        self.aug_info_dlg = InfoDialogAug()

    def passes_dialog(self):
        """

        :return:
        """
        self.passes_info_dlg = InfoDialogPasses()


class InfoDialogAug():

    def __init__(self):

        self.dlg = uic.loadUi("ImgAugDialog.ui")
        self.dlg.show()


class InfoDialogPasses():

    def __init__(self):

        self.dlg = uic.loadUi("PassesDialog.ui")
        self.dlg.show()


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle(QStyleFactory.create('Fusion'))
    form = Mainwindow()
    app.exec()