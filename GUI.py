import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon
from PyQt5.QtWidgets import QFileDialog, QTextEdit, QComboBox, QStyleFactory, QSpinBox, QLabel, QPushButton, QProgressBar, QMainWindow, QGraphicsEffect


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.openButton = QtWidgets.QPushButton(self)
        self.init_userinterface()

    def init_userinterface(self):
        self.setWindowTitle("Categorisation of Lepidoptera")
        self.attachtitle("Categorisation of Lepidoptera")
        self.setGeometry(100, 100, 1200, 800)
        self.setbackgroundimage("IMG/backgroundblur.jpg")
        self.setFixedSize(self.size())
        self.openButton.setText("Open Image")
        self.openButton.clicked.connect(self.openButton_click)
        self.openButton.move(325, 450)
        self.load_initial_images()
        self.show()
        app.setStyle(QStyleFactory.create('Fusion'))

        sys.exit(app.exec_())

    def attachtitle(self, titleName):
        """
        Used to attach the title to the window

        :param titleName: The title name
        :return:
        """
        titlelabel = QtWidgets.QLabel(self)
        titlelabel.setText(titleName)
        titlelabel.move(440, 10)
        font = QtGui.QFont("Times", 20, QtGui.QFont.Bold)
        titlelabel.setFont(font)

    def setbackgroundimage(self, imagepath):
        """
        Sets the background image for the window

        :param imagepath: path to the background image
        :return:
        """
        originalimage = QImage(imagepath)
        scaledimage = originalimage.scaled(QSize(1200, 800))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(scaledimage))
        self.setPalette(palette)

    def openButton_click(self):
        """
        handles the functionality for pressing the 'Open Image button on the UI

        :return:
        """

        self.comparison_image, _ = QFileDialog.getOpenFileName(self, "Open Image", "~", "Image Files (*.jpg *.png)")
        self.comparisonicon = QImage(self.comparison_image)
        self.comparisonscaledimage = self.comparisonicon.scaled(QSize(250, 250))
        self.comparisonimage = QtWidgets.QLabel(self)
        self.comparisonimage.setPixmap(QtGui.QPixmap.fromImage(self.comparisonscaledimage))
        self.comparisonimage.move(150, 180)
        self.edittextbox.setText(self.comparison_image)
        self.comparisonimage.show()

    def im_aug_info_window(self):
        """

        :return:
        """

        self.pwindow = SecondWindow()
        self.pwindow.setGeometry(500, 400, 500, 260)
        self.pwindow.setFixedSize(self.pwindow.size())
        self.pwindow.setWindowTitle("Image Augmentation Information")
        self.pwindow.show()

        #NEED TO RENAME VARS
        self.pwindow.comparisonicon = QImage("IMG/iamcats.png")
        self.pwindow.comparisonscaledimage = self.pwindow.comparisonicon.scaled(QSize(250, 250))
        self.pwindow.comparisonimage = QtWidgets.QLabel(self.pwindow)
        self.pwindow.comparisonimage.setPixmap(QtGui.QPixmap.fromImage(self.pwindow.comparisonscaledimage))
        self.pwindow.comparisonimage.setGeometry(250,5,250,250)
        self.pwindow.comparisonimage.show()




    def passes_info_window(self):
        """

        :return:
        """
        self.pawindow = SecondWindow()
        self.pawindow.setGeometry(100,100,500,400)
        self.pawindow.setFixedSize(self.pawindow.size())
        self.pawindow.setWindowTitle("Passes Information")
        self.pawindow.show()

        self.pawindow.comparisonicon = QImage("IMG/iamcats.png")
        self.pawindow.comparisonscaledimage = self.pawindow.comparisonicon.scaled(QSize(250, 250))
        self.pawindow.comparisonimage = QtWidgets.QLabel(self.pawindow)
        self.pawindow.comparisonimage.setPixmap(QtGui.QPixmap.fromImage(self.pawindow.comparisonscaledimage))
        self.pawindow.comparisonimage.setGeometry(250,5,250,250)
        self.pawindow.comparisonimage.show()



    def load_initial_images(self):
        """

        :return:
        """
        self.comparisonicon = QImage("S:/Edwin/Downloads/leedsbutterfly_dataset_v1.0/leedsbutterfly/images/0010025.png")
        self.comparisonscaledimage = self.comparisonicon.scaled(QSize(250, 250))
        self.comparisonimage = QtWidgets.QLabel(self)
        self.comparisonimage.setPixmap(QtGui.QPixmap.fromImage(self.comparisonscaledimage))
        self.comparisonimage.move(150, 180)
        self.comparisonimage.show()

        self.edittextbox = QTextEdit(self)
        self.edittextbox.setGeometry(150, 450, 150, 23)
        self.edittextbox.setText("No Image selected")
        self.edittextbox.setReadOnly(True)
        self.edittextbox.show()

        self.graphicon = QImage("IMG/nograph.png")
        self.graphscaledimage = self.graphicon.scaled(QSize(250, 250))
        self.graphimage = QtWidgets.QLabel(self)
        self.graphimage.setPixmap(QtGui.QPixmap.fromImage(self.graphscaledimage))
        self.graphimage.move(800, 180)
        self.graphimage.show()

        self.preprocessingcombobox = QComboBox(self)
        self.preprocessingcombobox.setGeometry(695, 180, 75, 23)
        self.preprocessingcombobox.addItem("YES")
        self.preprocessingcombobox.addItem("NO")

        self.passesspinbox = QSpinBox(self)
        self.passesspinbox.setGeometry(695, 240, 75, 23)
        self.passesspinbox.setMaximum(100000)
        self.passesspinbox.setValue(500)

        self.preprocessingcomboboxinfo = QLabel(self)
        self.passesspinboxinfo = QLabel(self)
        font = QtGui.QFont("Times", 10, QtGui.QFont.Bold)
        self.preprocessingcomboboxinfo.setGeometry(440,165,200,50)
        self.passesspinboxinfo.setGeometry(440,225,200,50)
        self.preprocessingcomboboxinfo.setText("With Image Augmentation?")
        self.passesspinboxinfo.setText("No. Of Passes")
        self.preprocessingcomboboxinfo.setFont(font)
        self.passesspinboxinfo.setFont(font)

        self.runbutton = QPushButton(self)
        self.runbutton.setText("Run Categorisation")
        self.runbutton.setGeometry(500, 575, 200, 100)

        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(100, 525, 1000, 25)
        self.progressbar.setValue(75)

        self.savegraphbutton = QPushButton(self)
        self.savegraphbutton.setText("Save Graph As Image")
        self.savegraphbutton.setGeometry(800,450,250,25)

        self.infoicon = QImage("IMG/info.png")
        self.infoimage = QPushButton(self)
        self.infoimage.setIcon(QIcon("IMG/info.png"))
        self.infoimage.setIconSize(QSize(20,20))
        self.infoimage.move(640, 180)
        self.infoimage.show()

        self.infoimage2 = QPushButton(self)
        self.infoimage2.setIcon(QIcon("IMG/info.png"))
        self.infoimage2.setIconSize(QSize(20,20))
        self.infoimage2.move(640, 240)
        self.infoimage2.show()

        self.infoimage.clicked.connect(self.im_aug_info_window)
        self.infoimage2.clicked.connect(self.passes_info_window)


class SecondWindow(QMainWindow):
    def __init__(self):
        super(SecondWindow, self).__init__()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    sys.exit(app.exec_())
