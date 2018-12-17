import  time, qtawesome as qta
from PyQt5 import QtCore, QtWidgets
from components import create, crypt, dab
from components.uiElements import seperator, passItem

class Passwords(QtWidgets.QWidget):
    #Global variables
    gPasswords = None

    def __init__(self):
        super(Passwords, self).__init__()

        #Password tab layouts
        vPassMain = QtWidgets.QHBoxLayout()
        vPassMain.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        vPExtras = QtWidgets.QVBoxLayout()
        vPExtras.setAlignment(QtCore.Qt.AlignTop)
        vPExtras.setSpacing(10)
 
        Passwords.gPasswords = QtWidgets.QGridLayout()
        vPassMain.addLayout(vPExtras)

        #Passwords structural widgets
        passScroll = QtWidgets.QScrollArea()
        passScroll.setWidgetResizable(True)
        wPassScroll = QtWidgets.QWidget()
        wPassScroll.setObjectName("passwordArea")
        wPassScroll.setLayout(Passwords.gPasswords)
        passScroll.setWidget(wPassScroll)

        vPassMain.addWidget(passScroll)

        #Create passwords tab
        leSearch = QtWidgets.QLineEdit()
        leSearch.setPlaceholderText("Search")
        leSearch.setMaximumWidth(300)
        vPExtras.addWidget(leSearch)

        sep = seperator.MenuSeperator()
        vPExtras.addWidget(sep)

        global lePassName
        lePassName = QtWidgets.QLineEdit()
        lePassName.setPlaceholderText("Name for Password")
        lePassName.setMaximumWidth(300)
        vPExtras.addWidget(lePassName)

        lEmail = QtWidgets.QLabel("Email Address")
        lEmail.setObjectName("smallLabel")
        vPExtras.addWidget(lEmail)

        global cbEmail
        cbEmail = QtWidgets.QComboBox()
        cbEmail.setEditable(True)
        cbEmail.setMaximumWidth(300)
        vPExtras.addWidget(cbEmail)

        global leUsername
        leUsername = QtWidgets.QLineEdit()
        leUsername.setPlaceholderText("Username")
        leUsername.setMaximumWidth(300)
        vPExtras.addWidget(leUsername)

        global leNewPass
        leNewPass = QtWidgets.QLineEdit()
        leNewPass.setPlaceholderText("Password")
        leNewPass.setMaximumWidth(300)
        vPExtras.addWidget(leNewPass)

        global chkGen
        chkGen = QtWidgets.QCheckBox("Generated")
        chkGen.setMaximumWidth(300)
        vPExtras.addWidget(chkGen)

        global chkTwoFA
        chkTwoFA = QtWidgets.QCheckBox("Uses 2FA")
        chkTwoFA.setMaximumWidth(300)
        vPExtras.addWidget(chkTwoFA)

        lCategory = QtWidgets.QLabel("Category")
        lCategory.setObjectName("smallLabel")
        vPExtras.addWidget(lCategory)

        global cbCategories
        cbCategories = QtWidgets.QComboBox()
        cbCategories.setMaximumWidth(300)
        vPExtras.addWidget(cbCategories)

        lBanner = QtWidgets.QLabel("Banner")
        lBanner.setObjectName("smallLabel")
        vPExtras.addWidget(lBanner)

        global cbBanner
        cbBanner = QtWidgets.QComboBox()
        cbBanner.setMaximumWidth(300)
        vPExtras.addWidget(cbBanner)

        global pteComment
        pteComment = QtWidgets.QTextEdit()
        pteComment.setPlaceholderText("Comment")
        pteComment.setMaximumWidth(300)
        pteComment.setMaximumHeight(100)
        pteComment.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))
        vPExtras.addWidget(pteComment)

        btnPWCreate = QtWidgets.QPushButton("Create New")
        btnPWCreate.setObjectName("btncreate")
        btnPWCreate.setMaximumWidth(300)
        #PasswordsName, email, Username, Password, 2fa, category, banner
        btnPWCreate.clicked.connect(lambda:Passwords.addPassword(
            self, lePassName.text(), 
            cbEmail.itemText(), 
            leUsername.text(), 
            leNewPass.text(), 
            chkGen.isChecked(), 
            chkTwoFA.isChecked(), 
            cbCategories.currentText(), 
            cbBanner.currentText(),
            pteComment.toPlainText()))
        vPExtras.addWidget(btnPWCreate)

        self.setLayout(vPassMain)

        #PasswordsName, email, Username, Password, 2fa, category, banner
    def addPassword(self, passName, emailAdd, theUsername, thePassword, generated, twoFAEnabled, theCategory, theBanner, theComment):
        #Check if the given email is already in the databse an add it if not
        duplicate = False
        emailData = dab.DatabaseActions.read(self, "configs", True)
        for i in range(len(emailData)):
            if emailData[i][2] == crypt.Encryption.encrypt(self, emailAdd):
                duplicate = True
        if not(duplicate):
            dab.DatabaseActions.insert(self, "configs", {'email':crypt.Encryption.encrypt(self, emailAdd)})

        insertionData = {"name":crypt.Encryption.encrypt(self, passName),
            "email":crypt.Encryption.encrypt(self, emailAdd),
            "uName":crypt.Encryption.encrypt(self, theUsername),
            "lstUsed":crypt.Encryption.encrypt(self, str(datetime.datetime.now())), 
            "gen":crypt.Encryption.encrypt(self, "False"), 
            "crypticPass":crypt.Encryption.encrypt(self, thePassword), 
            "twofactor":crypt.Encryption.encrypt(self, str(twoFAEnabled)), 
            "cat":crypt.Encryption.encrypt(self, theCategory), 
            "ban":crypt.Encryption.encrypt(self, theBanner),
            "comment":crypt.Encryption.encrypt(self, theComment)}
        dab.DatabaseActions.insert(self, "passwords", insertionData)
        CreateUI.clearData(self)
        CreateUI.setData(self, 1)


    def createPassSlates(self):
        create.CreateUI.updateProgressBar(self, 0)
        for i in reversed(range(Passwords.gPasswords.count())):
            Passwords.gPasswords.itemAt(i).widget().setParent(None)
            
        create.CreateUI.updateProgressBar(self, 5)

        row = 0
        column = 0
        #Ajust to the ammount of horizontal widgets
        widgetRowBreak = 4

        data = dab.DatabaseActions.read(self, table="passTable", everything=True)
        slateProgressIncrement = 80/len(data)
        startTime = time.time()
        for i in range(len(data)):
            passSlate = passItem.CreateUI()
            print("Decrypting password N°: {0}".format(i+1))
            #index, name, lastChanged, generated, banner="", email="", username="", category="generic", twoFa=False
            passSlate.setup(data[i][0], 
            crypt.Encryption.decrypt(self, data[i][1])[0], 
            crypt.Encryption.decrypt(self, data[i][5])[0], 
            crypt.Encryption.decrypt(self, data[i][6])[0], 
            crypt.Encryption.decrypt(self, data[i][7])[0], 
            crypt.Encryption.decrypt(self, data[i][2])[0], 
            crypt.Encryption.decrypt(self, data[i][3])[0], 
            crypt.Encryption.decrypt(self, data[i][4])[0], 
            crypt.Encryption.decrypt(self, data[i][8])[0])

            if column < widgetRowBreak:
                print("Adding slate at Row: {0}; Column: {1}".format(row, column))
                Passwords.gPasswords.addWidget(passSlate, row, column)
                column += 1
            else:
                row += 1
                column = 0
                Passwords.gPasswords.addWidget(passSlate, row, column)
                column +=1
            
            create.CreateUI.updateProgressBar(self, create.CreateUI.getProgressValue(self)+slateProgressIncrement)
        endTime = time.time()
        print("Time taken for decryption: {0}".format(round(endTime-startTime, 3)))
                
        #fill in all the comboboxes (email, categories, banners)
        startTime = time.time()
        print("Decrypting combobox data")
        cbEmail.addItem("None")
        dataEmail = dab.DatabaseActions.read(self, table="configs", everything=True)
        for i in range(len(dataEmail)):
            cbEmail.addItem(crypt.Encryption.decrypt(self, dataEmail[i][2])[0])
        create.CreateUI.updateProgressBar(self, create.CreateUI.getProgressValue(self)+5)

        dataCat = dab.DatabaseActions.read(self, table="categories", everything=True)
        for i in range(len(dataCat)):
            cbCategories.addItem(crypt.Encryption.decrypt(self, dataCat[i][1])[0])
        create.CreateUI.updateProgressBar(self, create.CreateUI.getProgressValue(self)+5)

        dataBanner = dab.DatabaseActions.read(self, table="banners", everything=True)
        for i in range(len(dataBanner)):
            cbBanner.addItem(crypt.Encryption.decrypt(self, dataBanner[i][1])[0])
        create.CreateUI.updateProgressBar(self, 100)
        endTime = time.time()
        print("Time taken for decryption: {0}".format(round(endTime-startTime, 3)))
        print("Passwords tab data set")
