import  datetime, time, qtawesome as qta
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

        global chkEncAll
        chkEncAll = QtWidgets.QCheckBox("Encrypt Everything")
        chkTwoFA.setMaximumWidth(300)
        vPExtras.addWidget(chkEncAll)

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
        
        global btnPWCreate
        btnPWCreate = QtWidgets.QPushButton("Create New")
        btnPWCreate.setObjectName("btncreate")
        btnPWCreate.setMaximumWidth(300)
        #PasswordsName, email, Username, Password, 2fa, category, banner
        btnPWCreate.clicked.connect(lambda:Passwords.addPassword(
            self, lePassName.text(), 
            cbEmail.currentText(), 
            leUsername.text(), 
            leNewPass.text(), 
            chkGen.isChecked(), 
            chkTwoFA.isChecked(), 
            cbCategories.currentText(), 
            cbBanner.currentText(),
            pteComment.toPlainText(),
            chkEncAll.isChecked()))
        vPExtras.addWidget(btnPWCreate)

        global btnPWUpdate
        btnPWUpdate = QtWidgets.QPushButton("Update")
        btnPWUpdate.setObjectName("btncreate")
        btnPWUpdate.setMaximumWidth(300)
        btnPWUpdate.setHidden(True)
        #PasswordsName, email, Username, Password, 2fa, category, banner
        btnPWUpdate.clicked.connect(lambda:Passwords.addPassword(
            self, lePassName.text(), 
            cbEmail.currentText(), 
            leUsername.text(), 
            leNewPass.text(), 
            chkGen.isChecked(), 
            chkTwoFA.isChecked(), 
            cbCategories.currentText(), 
            cbBanner.currentText(),
            pteComment.toPlainText(),
            chkEncAll.isChecked(),
            True))
        vPExtras.addWidget(btnPWUpdate)

        self.setLayout(vPassMain)

        #PasswordsName, email, Username, Password, 2fa, category, banner
    def addPassword(self, passName, emailAdd, theUsername, thePassword, generated, twoFAEnabled, theCategory, theBanner, theComment, encEverything, update=False, index=0):
        #Check if the given email is already in the databse an add it if not
        duplicate = False
        emailData = dab.DatabaseActions.read(self, "configs", True)
        encMailAdd = crypt.Encryption.encrypt(self, emailAdd)
        for i in range(len(emailData)):
            if emailData[i][2] == encMailAdd:
                duplicate = True
        if not(duplicate):
            dab.DatabaseActions.insert(self, "configs", {'name':"", 'email':crypt.Encryption.encrypt(self, emailAdd), 'dTest':"", 'keyLen':"", 'lstChanged':""})

        #If no username was give, use the email address as the username
        if theUsername == "":
            theUsername = emailAdd

        #Get the setting if the passwords should be salted
        config = dab.DatabaseActions.read(self, "configs", rows=1)
        decryptedData = crypt.Encryption.decrypt(self, config[0])

        #decide if everything or just the name, email, username and password should be encrypted and inserted
        if encEverything:
            insertionData = {"name":crypt.Encryption.encrypt(self, passName),
                "email":crypt.Encryption.encrypt(self, emailAdd),
                "uName":crypt.Encryption.encrypt(self, theUsername),
                "lstUsed":crypt.Encryption.encrypt(self, str(datetime.datetime.now())), 
                "gen":crypt.Encryption.encrypt(self, generated), 
                "crypticPass":crypt.Encryption.encrypt(self, thePassword), 
                "twofactor":crypt.Encryption.encrypt(self, str(twoFAEnabled)), 
                "cat":crypt.Encryption.encrypt(self, theCategory), 
                "ban":crypt.Encryption.encrypt(self, theBanner),
                "comment":crypt.Encryption.encrypt(self, theComment),
                "index":currentPassIndex,
                "salt":decryptedData[5]}
        else:
            insertionData = {"name":crypt.Encryption.encrypt(self, passName),
                "email":crypt.Encryption.encrypt(self, emailAdd),
                "uName":crypt.Encryption.encrypt(self, theUsername),
                "lstUsed":str(datetime.datetime.now()), 
                "gen":str(generated), 
                "crypticPass":crypt.Encryption.encrypt(self, thePassword), 
                "twofactor":str(twoFAEnabled), 
                "cat":str(theCategory), 
                "ban":str(theBanner),
                "comment":str(theComment),
                "index":currentPassIndex,
                "salt":decryptedData[5]}
        print(update)
        if update:
            dab.DatabaseActions.update(self, "passwords", insertionData)
        else:
            dab.DatabaseActions.insert(self, "passwords", insertionData)

        #Clear everything and repopulate, change later to only adding the new item!
        Passwords.clearData(self)
        Passwords.createPassSlates(self)

    def editPassword(self):
        """
        Rundown of all the data present
        self.index = passIndex
        self.name = name
        self.lastChanged = lastChanged
        self.generated = generated
        self.banner = banner
        self.email = email
        self.username = username
        self.category = category
        self.twoFa = twoFa
        """
        btnPWCreate.setHidden(True)
        btnPWUpdate.setHidden(False)
        global currentPassIndex
        currentPassIndex = self.index
        data = dab.DatabaseActions.read(self, table="passTable", rows=self.index)
        lPassword = crypt.Encryption.decrypt(self, data[9])[0]

        lePassName.setText(self.name)
        cbEmail.setCurrentIndex(cbEmail.findText(self.email))
        leUsername.setText(self.username)
        leNewPass.setText(lPassword)
        if self.generated == "True": chkGen.setChecked(True)
        else: chkGen.setChecked(False)
        if self.twoFa == "True": chkTwoFA.setChecked(True)
        else: chkTwoFA.setChecked(False)
        #chkEncAll needs to be implemented the long way because the variable isnt passed on!
        cbCategories.setCurrentIndex(cbCategories.findText(self.category))
        cbBanner.setCurrentIndex(cbBanner.findText(self.banner))
        pteComment.setText(self.comment)

    #Clears the list of the passwords
    def clearData(self):
        lePassName.setText("")
        leUsername.setText("")
        leNewPass.setText("")
        chkGen.setChecked(False)
        chkTwoFA.setChecked(False)
        pteComment.setText("")

    #Refine, that if nothing has changed nothing will be regenerated
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
        
        #loop through every added password
        for i in range(len(data)):
            passSlate = passItem.CreateUI()
            print("Decrypting password N°: {0}".format(i+1))

            #Array and tuple for keeping the order on the slate and for storing everything decrypted of an index
            decData = []
            readOrder = (0,1,5,6,7,2,3,4,8,10,11)

            #Loop for decrypting everything and testing if it actually needs to be decrypted
            for j in range(len(readOrder)):
                decrypt = crypt.Encryption.decrypt(self, data[i][readOrder[j]])
                if decrypt[1]:
                    decData.append(decrypt[0])
                else:
                    decData.append(data[i][readOrder[j]])

            #Note the password is fetched and decrypted in the passSlate widget based on the given index!
            passSlate.setup(decData[0], decData[1], decData[2], decData[3], decData[4], decData[5], decData[6], decData[7], decData[8], decData[9], decData[10])

            #decide where in the grid the new slate should be added.
            #Needs some math to base it on the width of the passScroll widget
            #Atm its just horizontal with scrolling
            """
            if column < widgetRowBreak:
                print("Adding slate at Row: {0}; Column: {1}".format(row, column))
                Passwords.gPasswords.addWidget(passSlate, row, column)
                column += 1
            else:
                row += 1
                column = 0
                Passwords.gPasswords.addWidget(passSlate, row, column)
                column +=1
            """
            Passwords.gPasswords.addWidget(passSlate, 0, i)
            
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
