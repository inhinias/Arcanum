from PyQt5 import QtCore, QtWidgets

class Keys(QtWidgets.QWidget):
    def __init__(self):
        super(Keys, self).__init__()
        
        #Keys tab layout
        hKeysMain = QtWidgets.QVBoxLayout()
        hKeysMain.setAlignment(QtCore.Qt.AlignTop)

        self.setLayout(hKeysMain)