import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush

#Globals
WindowHeight = 800
WindowWidth = 1200

def createWindow():
    """
    Used to create a blank window

    :return:
    """

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Categorisation of Lepidoptera")
    attachTitle("Categorisation of Lepidoptera", window)
    window.setGeometry(100, 100, WindowWidth, WindowHeight)
    setBackgroundImage("IMG/backgroundblur.jpg",window)
    window.show()
    sys.exit(app.exec_())


def attachTitle(titleName,window):
    """
    Used to attach the title to the window

    :param titleName: The title name
    :param window: The window to affix
    :return:
    """
    titlelabel = QtWidgets.QLabel(window)
    titlelabel.setText(titleName)
    titlelabel.move((WindowWidth/2)-180, 10)
    font = QtGui.QFont("Times", 20, QtGui.QFont.Bold)
    titlelabel.setFont(font)



def setBackgroundImage(imagepath, window):
    """
    Sets the background image for the window

    :param imagepath: path to the background image
    :param window: the target window
    :return:
    """
    originalImage = QImage(imagepath)
    scaledImage = originalImage.scaled(QSize(WindowWidth, WindowHeight))  # resize Image to widgets size
    palette = QPalette()
    palette.setBrush(10, QBrush(scaledImage))
    window.setPalette(palette)



createWindow()
