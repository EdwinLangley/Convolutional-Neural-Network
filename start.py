import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStyleFactory, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QSize
from cnn import NNet

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Mainwindow():

    def __init__(self):
        self.dlg = uic.loadUi("GUI.ui")
        self.dlg.run_cat.clicked.connect(self.run_category)
        self.dlg.open_target_btn.clicked.connect(self.open_image)
        self.dlg.run_train_btn.clicked.connect(self.run_train)
        self.dlg.imgaug_info_btn.clicked.connect(self.img_aug_dialog)
        self.dlg.passes_info_btn.clicked.connect(self.passes_dialog)
        self.dlg.load_model_btn.clicked.connect(self.load_model_handle)
        self.dlg.save_model_btn.clicked.connect(self.save_model_handle)
        self.dlg.show()

    def run_category(self):

        nn.make_prediction_on_model(self.comparison_image)
        nn.make_pie_chart()

        self.graph_image =  QImage("IMG/last_pie.png")
        self.graph_scaled_image = self.graph_image.scaled(QSize(630, 470))
        self.dlg.results_image.setPixmap(QPixmap.fromImage(self.graph_scaled_image))
        self.dlg.results_image.show()


    def open_image(self):
        """

        :return:
        """
        self.comparison_image, _ = QFileDialog.getOpenFileName(None, "Open Image", "~","Image Files (*.jpg *.png)")
        self.comparisonicon = QImage(self.comparison_image)
        self.comparisonscaledimage = self.comparisonicon.scaled(QSize(380, 380))
        self.dlg.selected_image.setPixmap(QPixmap.fromImage(self.comparisonscaledimage))
        self.dlg.target_img_src.setText(self.comparison_image)
        self.dlg.selected_image.show()


    def run_train(self):
        """

        :return:
        """

        nn.conv_pool_layers()
        nn.flattening()
        nn.full_connection()
        nn.gen_train_test()
        nn.fit_data_to_model()


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


    def load_model_handle(self):
        nn.load_model("model.h5")


    def save_model_handle(self):
        nn.save_model("model.h5")


class InfoDialogAug():

    def __init__(self):

        self.dlg = uic.loadUi("ImgAugDialog.ui")
        self.dlg.show()


class InfoDialogPasses():

    def __init__(self):

        self.dlg = uic.loadUi("PassesDialog.ui")
        self.dlg.show()



if __name__ == "__main__":
    nn = NNet()
    app = QApplication([])
    app.setStyle(QStyleFactory.create('Fusion'))
    form = Mainwindow()
    app.exec()