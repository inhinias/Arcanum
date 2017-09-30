from PyQt5 import QtGui, QtCore, QtWidgets
import seperator, dab, create
import qtawesome as qta

class CreateUI(QtWidgets.QWidget):
    def setup(self, placeText, cryptText, infoText, index):
        self.theIndex = index
        self.thePalce = create.CreateUI.place.text()
        self.theCrypt = create.CreateUI.newPass.text()
        self.theInfo = create.CreateUI.infoEdit.text()

        CreateUI.thePlace = placeText.decode()
        place = QtWidgets.QLabel(placeText.decode())
        place.setObjectName("listText")
        crypto = QtWidgets.QLabel(cryptText.decode())
        crypto.setObjectName("listText")
        info = QtWidgets.QLabel(infoText.decode())
        info.setObjectName("listText")
        cross = qta.icon("fa.times", color="#f9f9f9")
        editIcon = qta.icon("fa.pencil", color="#f9f9f9")
        deleteBtn = QtWidgets.QPushButton(cross, "")
        deleteBtn.setObjectName("deleteBtn")
        deleteBtn.clicked.connect(lambda:dab.Database.delete(self, self.theIndex))
        editBtn = QtWidgets.QPushButton(editIcon, "")
        editBtn.setObjectName("deleteBtn")
        editBtn.clicked.connect(lambda:dab.Database.update(self, self.theIndex, self.thePlace, self.theCrypt, self.theInfo))

        wMain = QtWidgets.QWidget()
        wMain.setObjectName("passColor")
        wEdit = QtWidgets.QWidget()
        wEdit.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred))

        #Layouts
        vBack = QtWidgets.QVBoxLayout()
        hMain = QtWidgets.QHBoxLayout()
        hEdit = QtWidgets.QHBoxLayout()

        vBack.setContentsMargins(QtCore.QMargins(0,0,0,0))
        hMain.setContentsMargins(QtCore.QMargins(10,5,10,5))
        hMain.setAlignment(QtCore.Qt.AlignLeft)
        hEdit.setContentsMargins(QtCore.QMargins(0,0,0,0))
        hEdit.setAlignment(QtCore.Qt.AlignRight)

        wMain.setLayout(hMain)
        wEdit.setLayout(hEdit)

        sep = seperator.MenuSeperator()
        sep.setup()
        sep2 = seperator.MenuSeperator()
        sep2.setup()
        sep3 = seperator.MenuSeperator()
        sep3.setup()

        hMain.addWidget(place)
        hMain.addWidget(sep)
        hMain.addWidget(crypto)
        hMain.addWidget(sep2)
        hMain.addWidget(info)
        hMain.addWidget(sep3)
        hEdit.addWidget(deleteBtn)
        #uncomment when fixed!
        #hEdit.addWidget(editBtn)
        hMain.addWidget(wEdit)
        vBack.addWidget(wMain)

        self.setLayout(vBack)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))