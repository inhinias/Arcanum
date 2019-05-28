from components import dab, create, crypt
from PyQt5 import QtCore, QtWidgets
import logging

class Settings(QtWidgets.QWidget):
    def __init__(self):
        super(Settings, self).__init__()   
        
        #Settings tab layouts
        gSettingsMain = QtWidgets.QGridLayout()
        gSettingsMain.setAlignment(QtCore.Qt.AlignTop)

        line = 0
        #Create the settings tab
        leEmail = QtWidgets.QLineEdit("")
        leEmail.setPlaceholderText("Email Address")
        leEmail.setMaximumWidth(300)

        btnAddMail = QtWidgets.QPushButton("Add")
        btnAddMail.setMaximumWidth(90)
        btnAddMail.setMaximumHeight(leEmail.sizeHint().height())
        btnAddMail.clicked.connect(lambda:Settings.addMailAddress(self, leEmail.text()))

        wAddMail = QtWidgets.QWidget()
        lAddMail = QtWidgets.QHBoxLayout()
        lAddMail.setAlignment(QtCore.Qt.AlignLeft)
        lAddMail.setContentsMargins(0,0,0,0)
        wAddMail.setLayout(lAddMail)

        lAddMail.addWidget(leEmail)
        lAddMail.addWidget(btnAddMail)
        gSettingsMain.addWidget(wAddMail, line, 0)

        line += 1
        global liAddresses
        liAddresses = QtWidgets.QListWidget()
        liAddresses.setMaximumWidth(400)
        liAddresses.setObjectName("emailList")
        gSettingsMain.addWidget(liAddresses, line, 0)

        self.setLayout(gSettingsMain)

    def createData(self):
        #Add all the email adresses!
        liAddresses.clear()
        dataEmail = dab.DatabaseActions.read(self, table="email", everything=True)
        for i in range(1, len(dataEmail)):
            liAddresses.addItem(crypt.Encryption.decrypt(self, dataEmail[i][1])[0])
        liAddresses.sortItems()
        logging.debug("Settings tab set")

    def addMailAddress(self, address):
        #Add the new email address to the database and update the list
        dab.DatabaseActions.insert(self, "email", {'emailAdd':crypt.Encryption.encrypt(self, address)})