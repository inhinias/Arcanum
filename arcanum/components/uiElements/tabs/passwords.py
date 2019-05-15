import  datetime, time, logging, qtawesome as qta
from PyQt5 import QtCore, QtWidgets
from components import create, crypt, dab
from components.uiElements import seperator, passItem
from components.uiElements.tabs import generator

class Passwords(QtWidgets.QWidget):
    #Global variables
    gPasswords = None
    leNewPass = None
    generated = False

    def __init__(self):
        super(Passwords, self).__init__()

        #Password tab layouts
        vPassMain = QtWidgets.QHBoxLayout()
        vPassMain.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)

        #The side layout with all the stuff to add/edit account data
        vPExtras = QtWidgets.QGridLayout()
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
        line = 0
        leSearch = QtWidgets.QLineEdit()
        leSearch.setPlaceholderText("Search")
        leSearch.setMaximumWidth(300)
        vPExtras.addWidget(leSearch, line,0)
        
        line += 1
        sep = seperator.MenuSeperator(300)
        vPExtras.addWidget(sep, line,0)

        line += 1
        global lePassName
        lePassName = QtWidgets.QLineEdit()
        lePassName.setPlaceholderText("Name for Password")
        lePassName.setMaximumWidth(300)
        vPExtras.addWidget(lePassName, line,0)

        line += 1
        lEmail = QtWidgets.QLabel("Email Address")
        lEmail.setObjectName("smallLabel")
        vPExtras.addWidget(lEmail, line,0)

        line += 1
        global cbEmail
        cbEmail = QtWidgets.QComboBox()
        cbEmail.setEditable(True)
        cbEmail.setMaximumWidth(300)
        vPExtras.addWidget(cbEmail, line,0)

        line += 1
        global leUsername
        leUsername = QtWidgets.QLineEdit()
        leUsername.setPlaceholderText("Username")
        leUsername.setMaximumWidth(300)
        vPExtras.addWidget(leUsername, line,0)

        wPassword = QtWidgets.QWidget()
        wPassword.setMaximumWidth(300)
        hPassword = QtWidgets.QHBoxLayout()
        hPassword.setAlignment(QtCore.Qt.AlignLeft)
        hPassword.setContentsMargins(0,0,0,0)
        wPassword.setLayout(hPassword)

        line += 1
        Passwords.leNewPass = QtWidgets.QLineEdit()
        Passwords.leNewPass.setPlaceholderText("Password")
        Passwords.leNewPass.setMaximumWidth(240)
        hPassword.addWidget(Passwords.leNewPass)

        btnGenPass = QtWidgets.QPushButton(qta.icon("fa.bolt", color="#f9f9f9"), "")
        btnGenPass.setMaximumSize(QtCore.QSize(50,50))
        btnGenPass.clicked.connect(lambda:Passwords.generatePassword(self))
        hPassword.addWidget(btnGenPass)

        vPExtras.addWidget(wPassword, line,0)

        """
        line += 1
        global chkGen
        chkGen = QtWidgets.QCheckBox("Generated")
        chkGen.setMaximumWidth(300)
        vPExtras.addWidget(chkGen, line,0)
        """

        line += 1
        global chkTwoFA
        chkTwoFA = QtWidgets.QCheckBox("Uses 2FA")
        chkTwoFA.setMaximumWidth(300)
        vPExtras.addWidget(chkTwoFA, line,0)

        line += 1
        global pteComment
        pteComment = QtWidgets.QTextEdit()
        pteComment.setPlaceholderText("Comment")
        pteComment.setMaximumWidth(300)
        pteComment.setMaximumHeight(100)
        pteComment.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))
        vPExtras.addWidget(pteComment, line,0)
        
        line += 1
        global btnPWCreate
        btnPWCreate = QtWidgets.QPushButton("Create New")
        btnPWCreate.setObjectName("btncreate")
        btnPWCreate.setMaximumWidth(300)

        #PasswordsName, email, Username, Password, 2fa
        btnPWCreate.clicked.connect(lambda:Passwords.addPassword(
            self, passName = lePassName.text(), 
            emailAdd = cbEmail.currentText(), 
            theUsername = leUsername.text(), 
            thePassword = Passwords.leNewPass.text(), 
            generated = Passwords.generated, 
            twoFAEnabled = chkTwoFA.isChecked(),
            theComment = pteComment.toPlainText(),
            update = False))
        vPExtras.addWidget(btnPWCreate, line,0)

        line += 1
        global btnPWUpdate
        btnPWUpdate = QtWidgets.QPushButton("Update")
        btnPWUpdate.setObjectName("btncreate")
        btnPWUpdate.setMaximumWidth(300)
        btnPWUpdate.setHidden(True)
        #PasswordsName, email, Username, Password, 2fa
        btnPWUpdate.clicked.connect(lambda:Passwords.addPassword(
            self, passName = lePassName.text(), 
            emailAdd = cbEmail.currentText(), 
            theUsername = leUsername.text(), 
            thePassword = Passwords.leNewPass.text(), 
            generated = Passwords.generated, 
            twoFAEnabled = chkTwoFA.isChecked(),
            theComment = pteComment.toPlainText(),
            update = True))
        vPExtras.addWidget(btnPWUpdate, line,0)

        self.setLayout(vPassMain)

        #PasswordsName, email, Username, Password, 2fa
    def addPassword(self, passName, emailAdd, theUsername, thePassword, generated, twoFAEnabled, theComment, update=False):
        #Check if the given email is already in the databse an add it if not
        duplicate = False
        emailData = dab.DatabaseActions.read(self, "email", True)
        #If no email was given do nothing
        if not(emailAdd == "None" or emailAdd == ""):
            #If there are no email addresses saved just skip the duplicate test and add the address
            if emailData != None:
                encMailAdd = crypt.Encryption.encrypt(self, emailAdd)
                for i in range(len(emailData)):
                    if emailData[i][1] == encMailAdd:
                        duplicate = True
                        emailAdd == i+1
                if not(duplicate):
                    dab.DatabaseActions.insert(self,
                        "email",
                        {'emailAdd':crypt.Encryption.encrypt(self, emailAdd)})
                    emailIndex = dab.DatabaseActions.getAmmount(self, "email")
            
            #Add the current email address because no other was present
            else:
                dab.DatabaseActions.insert(self,
                    "email",
                    {'emailAdd':crypt.Encryption.encrypt(self, emailAdd)})
                emailIndex = dab.DatabaseActions.getAmmount(self, "email")
        else:
            emailIndex = 1

        #If no username was give, one could use the email address as the username
        #But im not going to do so because the email addresses are in a diffrent table
        #and usernames aren't encrypted in the database

        #Note: Here used to be a split between if everything shuld be encrypted
        print(theComment)
        insertionData = {"name":crypt.Encryption.encrypt(self, passName), #The name is encrypted so no real account can be traced to the password.
            "email":emailIndex, #The email address is referenced here as an index to where it can be found in the email table
            "uName":str(theUsername), #Note: the username is not encrypted as it isn't a important part 
            "lstUsed":str(datetime.datetime.now()), #The last used timestamp will stay unencrypted to save resources
            "gen":str(generated), #The generated info can stay not encrypted as its non vital info
            "crypticPass":crypt.Encryption.encrypt(self, thePassword), #The most important thing of them all
            "twofactor":str(twoFAEnabled), #Meh, who cares to know if 2FA is used. It just sorts the more difficutl accounts out
            "comment":crypt.Encryption.encrypt(self, str(theComment))} #The comment on the account is encrypted as the user cannot be trusted to not have critical info in here

        if update:
            dab.DatabaseActions.update(self, "passwords", insertionData)
            logging.info("Password is being updated")
        else:
            logging.info("Password is being inserted")
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
        self.email = email
        self.username = username
        self.twoFa = twoFa
        """

        btnPWCreate.setHidden(True)
        btnPWUpdate.setHidden(False)
        global currentPassIndex
        currentPassIndex = self.index
        data = dab.DatabaseActions.read(self, table="passTable", row=self.index)
        lPassword = crypt.Encryption.decrypt(self, data[7])[0]

        lePassName.setText(self.name)
        cbEmail.setCurrentIndex(cbEmail.findText(self.email))
        leUsername.setText(self.username)
        Passwords.leNewPass.setText(lPassword)
        if self.twoFa == "True": chkTwoFA.setChecked(True)
        else: chkTwoFA.setChecked(False)
        pteComment.setText(self.comment)

    #Clears the list of the passwords
    def clearData(self):
        lePassName.setText("")
        leUsername.setText("")
        Passwords.leNewPass.setText("")
        chkTwoFA.setChecked(False)
        pteComment.setText("")

    #Refine, that if nothing has changed nothing will be regenerated
    def createPassSlates(self):
        #Delete all the password slates in order to add them again
        #Change later to only add the ones again which were changed
        for i in reversed(range(Passwords.gPasswords.count())):
            Passwords.gPasswords.itemAt(i).widget().setParent(None)

        #This is meant for the grid arrangement but not in use atm
        row = 0
        column = 0
        widgetRowBreak = 4

        #Get every password entry
        data = dab.DatabaseActions.read(self, table="passTable", everything=True)

        #Create the password displays only when there are passwords present
        if data == None:
            logging.info("No passwords present")

        else:
            #Store the start time to calculate the time taken for the decryption
            startTime = time.time()
            #loop through every added password
            for i in range(len(data)):
                passSlate = passItem.CreateUI()
                print("Decrypting password N° {0}".format(i+1))

                #Array and tuple for keeping the order on the slate and for storing everything decrypted of an index
                decData = []
                readOrder = (0,1,4,5,2,3,6,8)

                #Loop for decrypting everything and testing if it actually needs to be decrypted
                for j in range(len(readOrder)):
                    decrypt = crypt.Encryption.decrypt(self, data[i][readOrder[j]]) #Decrypt the current database index
                    if decrypt[1]: decData.append(decrypt[0]) #Append the decrypted data. No need to watch for read order. The line above takes care of that
                    else: decData.append(data[i][readOrder[j]]) #Get the current row data and append the wanted cell defined in the read order
                    
                
                #Note the password is fetched and decrypted in the passSlate widget based on the given index! IDK why?!
                #The email needs to be read from a diffrent table this here is just the index
                passSlate.setup(passIndex = decData[0],
                                name = decData[1],
                                lastChanged = decData[2],
                                generated = decData[3],
                                email = crypt.Encryption.decrypt(self, dab.DatabaseActions.read(self, "email", False, int(decData[4]))[1])[0],
                                username = decData[5],
                                twoFa  = decData[6],
                                comment = decData[7])

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
            
            endTime = time.time()
            print("Time taken for decryption: {0}".format(round(endTime-startTime, 3)))
                
        #fill in the combobox for the email addresses
        dataEmail = dab.DatabaseActions.read(self, table="email", everything=True)
        cbEmail.clear()
        for k in range(len(dataEmail)):
            email = crypt.Encryption.decrypt(self, dataEmail[k][1])[0]
            cbEmail.addItem(email)
        logging.info("Decrypted email addresses")
        print("Passwords tab data set")
    
    def generatePassword(self):
        gen = generator.Generator()