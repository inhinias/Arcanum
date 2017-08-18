from PyQt5 import QtGui, QtCore, QtWidgets

class MenuSeperator(QtWidgets.QWidget):
    def setup(self):
        vMenu = QtWidgets.QVBoxLayout()
        vMenu.setContentsMargins(QtCore.QMargins(0,0,0,0))

        wid = QtWidgets.QWidget()
        wid.setObjectName("seperator")
        wid.setMinimumHeight(3)
        wid.setMinimumWidth(3)
        wid.setMaximumWidth(3)
        vMenu.addWidget(wid)

        self.setLayout(vMenu)