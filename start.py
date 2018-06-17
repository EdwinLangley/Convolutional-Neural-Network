import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStyleFactory, QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QSize
from cnn import NNet

import ntpath

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
        """

        :return:
        """
        if nn.possible_to_run == True:
            nn.make_prediction_on_model(self.comparison_image)
            nn.make_pie_chart()

            self.graph_image =  QImage("IMG/last_pie.png")
            self.graph_scaled_image = self.graph_image.scaled(QSize(630, 470))
            self.dlg.results_image.setPixmap(QPixmap.fromImage(self.graph_scaled_image))
            self.dlg.results_image.show()
        else:
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.showMessage('Oh no! You don\'t seem to have a model loaded or trained.'
                                          ' You\'ll need to do this to '
                                          'run the categorisation')


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
        global nn
        if nn.possible_to_run == False:
            nn.conv_pool_layers()
            nn.flattening()
            nn.full_connection()
            nn.gen_train_test()
            nn.fit_data_to_model()
        else:
            self.qm = QMessageBox
            self.ret = self.qm.question(None, '', "This will overwrite the current trained model. Are you sure?", self.qm.Yes | self.qm.No)

            if self.ret == self.qm.Yes:
                nn = None
                nn = NNet()

                nn.conv_pool_layers()
                nn.flattening()
                nn.full_connection()
                nn.gen_train_test()
                nn.fit_data_to_model()

            if self.ret == self.qm.No:
                print("ignored")



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
        """

        :return:
        """
        self.model_path, _ = QFileDialog.getOpenFileName(None, "Open Model", "~", "Models (*.h5)")
        self.model_name = self.path_leaf(self.model_path)
        self.dlg.current_model_QTE.setText(self.model_name)
        nn.load_model(self.model_path)


    def save_model_handle(self):
        """

        :return:
        """

        self.save_model_name, _  = QFileDialog.getSaveFileName(None, "Save Model", "~", "Models (*.h5)")
        nn.save_model(self.save_model_name)


    def path_leaf(self, path):
        """

        :param path:
        :return:
        """
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)


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