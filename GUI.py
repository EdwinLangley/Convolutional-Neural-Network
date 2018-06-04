import sys
from PyQt5 import QtWidgets


#Function to create a window
def CreateWindow():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Categorisation of Lepidoptera")
    window.show()
    sys.exit(app.exec_())

CreateWindow()
