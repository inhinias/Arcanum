from PyQt5 import QtGui, QtCore, QtWidgets
from cryptography.fernet import Fernet
import dab, passItem, titlebar

class CreateUI:
    vPassList = None
    msg = None
    vHelper = None
    wPass = None
    scroll = None
    place = None
    newPass = None
    infoEdit = None
    def create(self):
        wMain = QtWidgets.QWidget()
        wMain.setObjectName("wMainColor")
        wAdd = QtWidgets.QWidget()
        wAdd.setObjectName("passTab")
        wAdd.setMaximumWidth(320)
        wAdd.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))
        CreateUI.wPass = QtWidgets.QWidget()
        CreateUI.wPass.setObjectName("passTab")
        CreateUI.wPass.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        wTitle = QtWidgets.QWidget()
        wTitle.setObjectName("Titlebar")
        self.wHelper = QtWidgets.QWidget()
        self.wHelper.setObjectName("passTab")
        self.wHelper.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))

        width = 300
        height = 30
        CreateUI.place = QtWidgets.QLineEdit("")
        CreateUI.place.setPlaceholderText("Place")
        CreateUI.place.setMaximumSize(QtCore.QSize(width, height))
        CreateUI.newPass = QtWidgets.QLineEdit("")
        CreateUI.newPass.setPlaceholderText("Password")
        CreateUI.newPass.setMaximumSize(QtCore.QSize(width, height))
        CreateUI.infoEdit = QtWidgets.QLineEdit("")
        CreateUI.infoEdit.setPlaceholderText("Additional information")
        CreateUI.infoEdit.setMaximumSize(QtCore.QSize(width, height))
        addBtn = QtWidgets.QPushButton("Add")
        addBtn.setMaximumSize(QtCore.QSize(width, height))
        addBtn.clicked.connect(lambda:CreateUI.addItem(self))

        CreateUI.scroll = QtWidgets.QScrollArea()
        CreateUI.scroll.setWidget(CreateUI.wPass)
        CreateUI.scroll.setWidgetResizable(True)

        #Layouts
        vBack = QtWidgets.QVBoxLayout()
        hMain = QtWidgets.QHBoxLayout()
        vAdd = QtWidgets.QVBoxLayout()
        CreateUI.vPassList = QtWidgets.QVBoxLayout()
        #CreateUI.hTitle = QtWidgets.QHBoxLayout()
        CreateUI.vHelper = QtWidgets.QVBoxLayout()

        CreateUI.vPassList.setAlignment(QtCore.Qt.AlignTop)
        hMain.setAlignment(QtCore.Qt.AlignTop)
        vAdd.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        vBack.setContentsMargins(QtCore.QMargins(0,0,0,0))
        CreateUI.vHelper.setContentsMargins(QtCore.QMargins(0,0,0,0))
        CreateUI.vHelper.setSpacing(0)
        CreateUI.vPassList.setSpacing(3)

        #wTitle.setLayout(CreateUI.hTitle)
        wMain.setLayout(hMain)
        CreateUI.wPass.setLayout(CreateUI.vPassList)
        wAdd.setLayout(vAdd)
        self.wHelper.setLayout(CreateUI.vHelper)

        vAdd.addWidget(CreateUI.place)
        vAdd.addWidget(CreateUI.newPass)
        vAdd.addWidget(CreateUI.infoEdit)
        vAdd.addWidget(addBtn)
        hMain.addWidget(wAdd)
        hMain.addWidget(self.wHelper)
        vBack.addWidget(wMain)

        self.setLayout(vBack)

    def addItem(self):
            dab.Database.insert(self, CreateUI.place.text(), CreateUI.newPass.text(), CreateUI.infoEdit.text())
            CreateUI.populateList(self)
            CreateUI.place.setText("")
            CreateUI.newPass.setText("")
            CreateUI.infoEdit.setText("")

    def populateList(self):
            for i in reversed(range(CreateUI.vPassList.count())):
                CreateUI.vPassList.itemAt(i).widget().setParent(None)
            for i in reversed(range(CreateUI.vHelper.count())): 
                CreateUI.vHelper.itemAt(i).widget().setParent(None)

            len = dab.Database.length(self)
            for i in range(len):
                dabItem = dab.Database.read(self, i)
                if i == 0:
                    titleWid = titlebar.CreateUI()
                    f = Fernet(dab.Database.key)
                    string = ""
                    f.encrypt(string.encode())

                    try:
                        titleWid.setup(f.decrypt(dabItem[1].encode()), f.decrypt(dabItem[2].encode()), f.decrypt(dabItem[3].encode()))
                        CreateUI.vHelper.addWidget(titleWid)
                    
                    except:
                        titleWid.setup(f.decrypt(dabItem[1]), f.decrypt(dabItem[2]), f.decrypt(dabItem[3]))
                        CreateUI.vHelper.addWidget(titleWid)
                    
                    CreateUI.vHelper.addWidget(CreateUI.scroll)

                else:
                    passWid = passItem.CreateUI()
                    f = Fernet(dab.Database.key)

                    try:
                        passWid.setup(f.decrypt(dabItem[1].encode()), f.decrypt(dabItem[2].encode()), f.decrypt(dabItem[3].encode()), dabItem[0])
                        CreateUI.vPassList.addWidget(passWid)
                    except:
                        passWid.setup(f.decrypt(dabItem[1]), f.decrypt(dabItem[2]), f.decrypt(dabItem[3]), dabItem[0])
                        CreateUI.vPassList.addWidget(passWid)