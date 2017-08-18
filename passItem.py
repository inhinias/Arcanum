from PyQt5 import QtGui, QtCore, QtWidgets
import seperator

class CreateUI(QtWidgets.QWidget):
    def setup(self, placeText, cryptText, infoText):
        place = QtWidgets.QLabel(placeText.decode())
        place.setObjectName("listText")
        crypto = QtWidgets.QLabel(cryptText.decode())
        crypto.setObjectName("listText")
        info = QtWidgets.QLabel(infoText.decode())
        info.setObjectName("listText")

        wMain = QtWidgets.QWidget()
        wMain.setObjectName("passColor")

        #Layouts
        vBack = QtWidgets.QVBoxLayout()
        hMain = QtWidgets.QHBoxLayout()

        vBack.setContentsMargins(QtCore.QMargins(0,0,0,0))
        hMain.setContentsMargins(QtCore.QMargins(10,5,10,5))
        hMain.setAlignment(QtCore.Qt.AlignLeft)

        wMain.setLayout(hMain)

        sep = seperator.MenuSeperator()
        sep.setup()
        sep2 = seperator.MenuSeperator()
        sep2.setup()

        hMain.addWidget(place)
        hMain.addWidget(sep)
        hMain.addWidget(crypto)
        hMain.addWidget(sep2)
        hMain.addWidget(info)
        vBack.addWidget(wMain)

        self.setLayout(vBack)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))