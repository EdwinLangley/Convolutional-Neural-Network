import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QFileDialog, QTextEdit, QComboBox, QStyleFactory, QSpinBox, QLabel, QPushButton


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
        self.openButton.move(375, 450)
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
        self.comparisonimage.move(200, 180)
        self.edittextbox.setText(self.comparison_image)
        self.comparisonimage.show()


    def load_initial_images(self):
        """

        :return:
        """
        self.comparisonicon = QImage("S:/Edwin/Downloads/leedsbutterfly_dataset_v1.0/leedsbutterfly/images/0010025.png")
        self.comparisonscaledimage = self.comparisonicon.scaled(QSize(250, 250))
        self.comparisonimage = QtWidgets.QLabel(self)
        self.comparisonimage.setPixmap(QtGui.QPixmap.fromImage(self.comparisonscaledimage))
        self.comparisonimage.move(200, 180)
        self.comparisonimage.show()

        self.edittextbox = QTextEdit(self)
        self.edittextbox.setGeometry(200, 450, 150, 23)
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
        self.preprocessingcombobox.setGeometry(675, 180, 75, 23)
        self.preprocessingcombobox.addItem("YES")
        self.preprocessingcombobox.addItem("NO")

        self.passesspinbox = QSpinBox(self)
        self.passesspinbox.setGeometry(675, 240, 75, 23)
        self.passesspinbox.setMaximum(100000)
        self.passesspinbox.setValue(500)

        self.preprocessingcomboboxinfo = QLabel(self)
        self.passesspinboxinfo = QLabel(self)
        font = QtGui.QFont("Times", 10, QtGui.QFont.Bold)
        self.preprocessingcomboboxinfo.setGeometry(490,165,150,50)
        self.passesspinboxinfo.setGeometry(490,225,150,50)
        self.preprocessingcomboboxinfo.setText("With Pre-Processing?")
        self.passesspinboxinfo.setText("No. Of Passes")
        self.preprocessingcomboboxinfo.setFont(font)
        self.passesspinboxinfo.setFont(font)

        self.runbutton = QPushButton(self)
        self.runbutton.setText("Run Categorisation")
        self.runbutton.setGeometry(500, 575, 200, 100)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    sys.exit(app.exec_())
