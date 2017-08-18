from PyQt5 import QtGui, QtCore, QtWidgets
from cryptography.fernet import Fernet
import dab, passItem

class CreateUI:
    vPassList = None
    msg = None
    def create(self):
        wMain = QtWidgets.QWidget()
        wMain.setObjectName("wMainColor")
        wAdd = QtWidgets.QWidget()
        wAdd.setObjectName("passTab")
        wAdd.setMaximumWidth(320)
        wAdd.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))
        wPass = QtWidgets.QWidget()
        wPass.setObjectName("passTab")
        wPass.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))

        width = 300
        height = 30
        self.place = QtWidgets.QLineEdit("")
        self.place.setPlaceholderText("Place")
        self.place.setMaximumSize(QtCore.QSize(width, height))
        self.newPass = QtWidgets.QLineEdit("")
        self.newPass.setPlaceholderText("Password")
        self.newPass.setMaximumSize(QtCore.QSize(width, height))
        self.infoEdit = QtWidgets.QLineEdit("")
        self.infoEdit.setPlaceholderText("Additional information")
        self.infoEdit.setMaximumSize(QtCore.QSize(width, height))
        addBtn = QtWidgets.QPushButton("Add")
        addBtn.setMaximumSize(QtCore.QSize(width, height))
        addBtn.clicked.connect(lambda:CreateUI.addItem(self))

        scroll = QtWidgets.QScrollArea()
        scroll.setWidget(wPass)
        scroll.setWidgetResizable(True)

        #Layouts
        vBack = QtWidgets.QVBoxLayout()
        hMain = QtWidgets.QHBoxLayout()
        vAdd = QtWidgets.QVBoxLayout()
        CreateUI.vPassList = QtWidgets.QVBoxLayout()

        CreateUI.vPassList.setAlignment(QtCore.Qt.AlignTop)
        hMain.setAlignment(QtCore.Qt.AlignTop)
        vAdd.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        vBack.setContentsMargins(QtCore.QMargins(0,0,0,0))
        CreateUI.vPassList.setSpacing(3)

        wMain.setLayout(hMain)
        wPass.setLayout(CreateUI.vPassList)
        wAdd.setLayout(vAdd)
        
        vAdd.addWidget(self.place)
        vAdd.addWidget(self.newPass)
        vAdd.addWidget(self.infoEdit)
        vAdd.addWidget(addBtn)
        hMain.addWidget(wAdd)
        hMain.addWidget(scroll)
        vBack.addWidget(wMain)

        self.setLayout(vBack)

    def addItem(self):
            dab.Database.insert(self, self.place.text(), self.newPass.text(), self.infoEdit.text())
            CreateUI.populateList(self)
            self.place.setText("")
            self.newPass.setText("")
            self.infoEdit.setText("")

    def populateList(self):
            for i in reversed(range(CreateUI.vPassList.count())): 
                CreateUI.vPassList.itemAt(i).widget().setParent(None)

            len = dab.Database.length(self)
            for i in range(len):
                dabItem = dab.Database.read(self, i)
                passWid = passItem.CreateUI()

                f = Fernet(dab.Database.key)
                passWid.setup(f.decrypt(dabItem[1]), f.decrypt(dabItem[2]), f.decrypt(dabItem[3]))
                CreateUI.vPassList.addWidget(passWid)