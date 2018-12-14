from PyQt5 import QtCore, QtWidgets

class Generator(QtWidgets.QWidget):
    def __init__(self):
        super(Generator, self).__init__()

        #Generator tab layouts
        vGeneratorMain = QtWidgets.QVBoxLayout()
        vGeneratorMain.setAlignment(QtCore.Qt.AlignTop)

        self.setLayout(vGeneratorMain)