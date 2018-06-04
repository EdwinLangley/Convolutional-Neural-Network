import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_userinterface()

    def init_userinterface(self):
        self.setWindowTitle("Categorisation of Lepidoptera")
        self.attachtitle("Categorisation of Lepidoptera")
        self.setGeometry(100, 100, 1200, 800)
        self.setbackgroundimage("IMG/backgroundblur.jpg")
        self.setFixedSize(self.size())
        self.show()
        sys.exit(app.exec_())

    def attachtitle(self, titleName):
        """
        Used to attach the title to the window

        :param titleName: The title name
        :param window: The window to affix
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

    def btn_click(self):
        self.l.setText('I have been clicked')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    sys.exit(app.exec_())
