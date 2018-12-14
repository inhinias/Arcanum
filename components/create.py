import  datetime, time, qtawesome as qta
from PyQt5 import QtGui, QtCore, QtWidgets
from components.uiElements.tabs import overview, passwords
from components import dab, crypt
from components.uiElements import passItem, seperator

class CreateUI:
    vPassList = None
    msg = None
    vHelper = None
    wPass = None
    scroll = None
    place = None
    newPass = None
    infoEdit = None
    password = ""
    emailAddress = "kenneth.mathis99@gmail.com"
    def create(self):
        #Layouts
        #Main Layouts
        vBack = QtWidgets.QVBoxLayout() #Backbone layout for color at the lowest level
        vBack.setContentsMargins(0,0,0,0)
        vMain = QtWidgets.QVBoxLayout() #Layouts for the main stuff
        hMain = QtWidgets.QHBoxLayout()
        vMain.setContentsMargins(0,0,0,0)
        hMain.setContentsMargins(5,0,5,5)
        vToolRack = QtWidgets.QVBoxLayout() #Layout of the rack on the side
        vToolRack.setAlignment(QtCore.Qt.AlignTop)
        self.sCentral = QtWidgets.QStackedLayout()

        #Overview tab layouts
        hOverview = QtWidgets.QHBoxLayout()
        hOverview.setAlignment(QtCore.Qt.AlignVCenter)
        hOverview.setSpacing(20)

        gStrength = QtWidgets.QGridLayout()
        gStrength.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        gStrength.setContentsMargins(10,10,10,10)

        gStats = QtWidgets.QGridLayout()
        gStats.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        gStats.setContentsMargins(10,10,10,10)

        vOCenter = QtWidgets.QVBoxLayout()
        vOCenter.setSpacing(50)
        vOCenter.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        #Password tab layouts
        vPassMain = QtWidgets.QHBoxLayout()
        vPassMain.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        vPExtras = QtWidgets.QVBoxLayout()
        vPExtras.setAlignment(QtCore.Qt.AlignTop)
        vPExtras.setSpacing(10)

        global gPasswords 
        gPasswords = QtWidgets.QGridLayout()
        vPassMain.addLayout(vPExtras)

        #Generator tab layouts
        vGeneratorMain = QtWidgets.QVBoxLayout()
        vGeneratorMain.setAlignment(QtCore.Qt.AlignTop)

        wGenerator = QtWidgets.QWidget()
        wGenerator.setLayout(vGeneratorMain)

        #Notes tab layouts
        hNotesMain = QtWidgets.QHBoxLayout()
        hNotesMain.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)

        hCreateNote = QtWidgets.QHBoxLayout()
        hCreateNote.setAlignment(QtCore.Qt.AlignTop)
        hCreateNote.setSpacing(10)
        hNotesMain.addLayout(hCreateNote)

        wNotesMain = QtWidgets.QWidget()
        wNotesMain.setLayout(hNotesMain)

        #Bunkers tab layout
        hBunkersMain = QtWidgets.QVBoxLayout()
        hBunkersMain.setAlignment(QtCore.Qt.AlignTop)

        wBunkersMain = QtWidgets.QWidget()
        wBunkersMain.setLayout(hBunkersMain)


        #Settings tab layouts
        gSettingsMain = QtWidgets.QGridLayout()
        gSettingsMain.setAlignment(QtCore.Qt.AlignTop)

        wSettings = QtWidgets.QWidget()
        wSettings.setLayout(gSettingsMain)


        #Structural widgets and stuff from layouts
        #Overview
        wOverview = QtWidgets.QWidget()
        wOverview.setLayout(hOverview)

        wOCenter = QtWidgets.QWidget()
        """wOCenter.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))"""
        wOCenter.setLayout(vOCenter)

        #Passwords
        passScroll = QtWidgets.QScrollArea()
        passScroll.setWidgetResizable(True)
        wPassScroll = QtWidgets.QWidget()
        wPassScroll.setLayout(gPasswords)
        passScroll.setWidget(wPassScroll)

        vPassMain.addWidget(passScroll)

        wPasswords = QtWidgets.QWidget()
        wPasswords.setLayout(vPassMain)

        #There may be some lines here for the following tabs but not at the moment
        #Generator
        #Notes
        #Bunkers
        #Settings

        #Combine the pages of the sCentral layout
        self.sCentral.addWidget(wOverview)
        self.sCentral.addWidget(wPasswords)
        self.sCentral.addWidget(wGenerator)
        self.sCentral.addWidget(wNotesMain)
        self.sCentral.addWidget(wBunkersMain)
        self.sCentral.addWidget(wSettings)

        #Widget in the main layout for the background colour
        wBack = QtWidgets.QWidget()
        wBack.setObjectName("wMain")
        wBack.setLayout(vMain)
        vBack.addWidget(wBack)

        wToolRack = QtWidgets.QWidget()
        wToolRack.setObjectName("wRack")
        wToolRack.setMinimumWidth(200)
        wToolRack.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))
        wToolRack.setLayout(vToolRack)
        hMain.addWidget(wToolRack)

        wCentral = QtWidgets.QWidget()
        wCentral.setObjectName("wCentral")
        wCentral.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        wCentral.setLayout(self.sCentral)
        hMain.addWidget(wCentral)

        #Titlebar stuff
        tbLay = QtWidgets.QHBoxLayout()
        tbLay.setAlignment(QtCore.Qt.AlignRight)
        tbLay.setContentsMargins(0,0,0,0)
        tbWid = QtWidgets.QWidget()
        tbWid.setObjectName("titlebar")
        tbWid.setLayout(tbLay)
        
        mini = QtWidgets.QPushButton(qta.icon("fa.minus", color="#f9f9f9"), "")
        mini.setObjectName("minimize")
        mini.setMinimumSize(QtCore.QSize(30,30))
        """mini.clicked.connect(CreateUI.minimize(self))"""
        tbLay.addWidget(mini)

        quitBtn = QtWidgets.QPushButton(qta.icon("fa.times", color="#f9f9f9"), "")
        quitBtn.setObjectName("quitBtn")
        quitBtn.setMinimumSize(QtCore.QSize(30,30))
        quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        tbLay.addWidget(quitBtn)

        vMain.addWidget(tbWid)
        vMain.addLayout(hMain)
        
        #Populate the rack on the side
        rackBtnMinheight = 50
        rackIcoSize = QtCore.QSize(32, 32)
        btnOverview = QtWidgets.QPushButton(qta.icon("fa.compass", color="#f9f9f9"), "Overview")
        btnPasswords = QtWidgets.QPushButton(qta.icon("fa.lock", color="#f9f9f9"), "Passwords")
        btnGenerate = QtWidgets.QPushButton(qta.icon("fa.bolt", color="#f9f9f9"), "Generator")
        btnNotes = QtWidgets.QPushButton(qta.icon("fa.paperclip", color="#f9f9f9"), "Notes")
        btnBunkers = QtWidgets.QPushButton(qta.icon("fa.university", color="#f9f9f9"), "Bunkers")
        btnSettings = QtWidgets.QPushButton(qta.icon("fa.cog", color="#f9f9f9"), "Settings")

        btnOverview.setMinimumHeight(rackBtnMinheight)
        btnPasswords.setMinimumHeight(rackBtnMinheight)
        btnGenerate.setMinimumHeight(rackBtnMinheight)
        btnNotes.setMinimumHeight(rackBtnMinheight)
        btnBunkers.setMinimumHeight(rackBtnMinheight)
        btnSettings.setMinimumHeight(rackBtnMinheight)

        btnOverview.setIconSize(rackIcoSize)
        btnPasswords.setIconSize(rackIcoSize)
        btnGenerate.setIconSize(rackIcoSize)
        btnNotes.setIconSize(rackIcoSize)
        btnBunkers.setIconSize(rackIcoSize)
        btnSettings.setIconSize(rackIcoSize)

        btnOverview.clicked.connect(lambda:CreateUI.switchTab(self, 0))
        btnPasswords.clicked.connect(lambda:CreateUI.switchTab(self, 1))
        btnGenerate.clicked.connect(lambda:CreateUI.switchTab(self, 2))
        btnNotes.clicked.connect(lambda:CreateUI.switchTab(self, 3))
        btnBunkers.clicked.connect(lambda:CreateUI.switchTab(self, 4))
        btnSettings.clicked.connect(lambda:CreateUI.switchTab(self, 5))

        global prgWorking
        prgWorking = QtWidgets.QProgressBar()
        prgWorking.setTextVisible(False)
        prgWorking.setValue(0)
        prgWorking.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))
        
        vToolRack.addWidget(btnOverview)
        vToolRack.addWidget(btnPasswords)
        vToolRack.addWidget(btnGenerate)
        vToolRack.addWidget(btnNotes)
        vToolRack.addWidget(btnBunkers)
        vToolRack.addWidget(btnSettings)
        vToolRack.addWidget(prgWorking)

        #Create the overview page
        #Strength overview
        strengthLvls = ["Very Weak","Weak","Acceptable","Strong","Very Strong","Fort Knox"]
        for i in range(len(strengthLvls)):
            sLabel = QtWidgets.QLabel(strengthLvls[i] + ":")
            sLabel.setObjectName("oText")
            gStrength.addWidget(sLabel,i,0)
        
        global tVeryWeak
        global tWeak
        global tAcceptable
        global tStrong
        global tVeryStrong
        global tFortKnox

        tVeryWeak = QtWidgets.QLabel("0")
        tVeryWeak.setObjectName("oText")
        gStrength.addWidget(tVeryWeak,0,1)

        tWeak = QtWidgets.QLabel("0")
        tWeak.setObjectName("oText")
        gStrength.addWidget(tWeak,1,1)

        tAcceptable = QtWidgets.QLabel("0")
        tAcceptable.setObjectName("oText")
        gStrength.addWidget(tAcceptable,2,1)

        tStrong = QtWidgets.QLabel("0")
        tStrong.setObjectName("oText")
        gStrength.addWidget(tStrong,3,1)

        tVeryStrong = QtWidgets.QLabel("0")
        tVeryStrong.setObjectName("oText")
        gStrength.addWidget(tVeryStrong,4,1)

        tFortKnox = QtWidgets.QLabel("0")
        tFortKnox.setObjectName("oText")
        gStrength.addWidget(tFortKnox,5,1)
        
        tNPassText = QtWidgets.QLabel("Passwords Stored")
        tNPassText.setObjectName("pStoredText")
        tNPassText.setAlignment(QtCore.Qt.AlignHCenter)
        vOCenter.addWidget(tNPassText)

        global tNumPasswords
        tNumPasswords = QtWidgets.QLabel("000000")
        tNumPasswords.setObjectName("numPasswords")
        vOCenter.addWidget(tNumPasswords)

        statTexts = ["Reused","Forgotten","Generated","2FA","In RockYou","Leaked"]
        for j in range(len(statTexts)):
            sStats = QtWidgets.QLabel(statTexts[j] + ":")
            sStats.setObjectName("oText")
            gStats.addWidget(sStats,j,0)

        global tReused
        global tForgotten
        global tGen
        global tTwoFA
        global tRockYou
        global tLeaked

        tReused = QtWidgets.QLabel("0")
        tReused.setObjectName("oText")
        gStats.addWidget(tReused,0,1)

        tForgotten = QtWidgets.QLabel("0")
        tForgotten.setObjectName("oText")
        gStats.addWidget(tForgotten,1,1)

        tGen = QtWidgets.QLabel("0")
        tGen.setObjectName("oText")
        gStats.addWidget(tGen,2,1)

        tTwoFA = QtWidgets.QLabel("0")
        tTwoFA.setObjectName("oText")
        gStats.addWidget(tTwoFA,3,1)

        tRockYou = QtWidgets.QLabel("0")
        tRockYou.setObjectName("oText")
        gStats.addWidget(tRockYou,4,1)

        tLeaked = QtWidgets.QLabel("0")
        tLeaked.setObjectName("oText")
        gStats.addWidget(tLeaked,5,1)

        hOverview.addLayout(gStrength)
        hOverview.addWidget(wOCenter)
        hOverview.addLayout(gStats)

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
        btnPWCreate.clicked.connect(lambda:CreateUI.addPassword(
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

        #Create the generator tab


        #Create the settings tab
        leEmail = QtWidgets.QLineEdit(CreateUI.emailAddress)
        leEmail.setPlaceholderText("Email Address")
        leEmail.setMaximumWidth(300)
        gSettingsMain.addWidget(leEmail, 0, 0)

        btnUpdateMail = QtWidgets.QPushButton("Add")
        btnUpdateMail.setMaximumWidth(100)
        btnUpdateMail.setMaximumHeight(leEmail.sizeHint().height())
        btnUpdateMail.clicked.connect(lambda:CreateUI.addMailAddress(self, leEmail.text()))
        gSettingsMain.addWidget(btnUpdateMail, 0, 1)

        global liAddresses
        liAddresses = QtWidgets.QListWidget()
        liAddresses.setMaximumWidth(400)
        gSettingsMain.addWidget(liAddresses, 1, 0)

        self.setLayout(vBack)

    def addMailAddress(self, address):
        #name, email, dTest, keyLen, lstChanged
        #Add option later to encryt everything even if it is empty
        insertionData = {"name":"",
            "email":crypt.Encryption.encrypt(self, address),
            "dTest":"",
            "keyLen":"", 
            "lstChanged":""}
        dab.DatabaseActions.insert(self, "configs", insertionData)

    def setData(self, tab):
        #Overview
        if tab == 0:
            CreateUI.updateProgressBar(self, 0)
            numPass = dab.DatabaseActions.getAmmount(self, "passwords")
            print("Currently {0} passwords stored".format(numPass))
            CreateUI.updateProgressBar(self, 50)
            if numPass == 0:
                tNumPasswords.setText("000000")
            elif len(str(numPass)) >= 6:
                tNumPasswords.setText(str(numPass))
            elif len(str(numPass)) == 5:
                tNumPasswords.setText("0" + str(numPass))
            elif len(str(numPass)) == 4:
                tNumPasswords.setText("00" + str(numPass))
            elif len(str(numPass)) == 3:
                tNumPasswords.setText("000" + str(numPass))
            elif len(str(numPass)) == 2:
                tNumPasswords.setText("0000" + str(numPass))
            elif len(str(numPass))== 1:
                tNumPasswords.setText("00000" + str(numPass))
            else:
                print("Error with adding 0 to the numPass number")
            
            CreateUI.updateProgressBar(self, 100)
            print("Overview data set")

        #Passwords
        elif tab == 1:
            CreateUI.updateProgressBar(self, 0)
            for i in reversed(range(gPasswords.count())):
                gPasswords.itemAt(i).widget().setParent(None)
            
            CreateUI.updateProgressBar(self, 5)

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
                    gPasswords.addWidget(passSlate, row, column)
                    column += 1
                else:
                    row += 1
                    column = 0
                    gPasswords.addWidget(passSlate, row, column)
                    column +=1
            
                CreateUI.updateProgressBar(self, prgWorking.value()+slateProgressIncrement)
            endTime = time.time()
            print("Time taken for decryption: {0}".format(round(endTime-startTime, 3)))
                
            #fill in all the comboboxes (email, categories, banners)
            startTime = time.time()
            print("Decrypting combobox data")
            cbEmail.addItem("None")
            dataEmail = dab.DatabaseActions.read(self, table="configs", everything=True)
            for i in range(len(dataEmail)):
                cbEmail.addItem(crypt.Encryption.decrypt(self, dataEmail[i][2])[0])
            CreateUI.updateProgressBar(self, prgWorking.value()+5)

            dataCat = dab.DatabaseActions.read(self, table="categories", everything=True)
            for i in range(len(dataCat)):
                cbCategories.addItem(crypt.Encryption.decrypt(self, dataCat[i][1])[0])
            CreateUI.updateProgressBar(self, prgWorking.value()+5)

            dataBanner = dab.DatabaseActions.read(self, table="banners", everything=True)
            for i in range(len(dataBanner)):
                cbBanner.addItem(crypt.Encryption.decrypt(self, dataBanner[i][1])[0])
            CreateUI.updateProgressBar(self, 100)
            endTime = time.time()
            print("Time taken for decryption: {0}".format(round(endTime-startTime, 3)))

            print("Passwords tab data set")

        #Generators not needed
        elif tab == 2:
            print("Generator tab needs nothing to be set")

        #Notes
        elif tab == 3:
            print("Notes tab data set")

        #Bunkers
        elif tab == 4:
            print("Bunkers tab set")

        #Settings
        elif tab == 5:
            liAddresses.clear()
            dataEmail = dab.DatabaseActions.read(self, table="configs", everything=True)
            for i in range(len(dataEmail)):
                liAddresses.addItem(crypt.Encryption.decrypt(self, dataEmail[i][2])[0])
                if i == 0:
                    CreateUI.updateProgressBar(self, 0)
                else:
                    CreateUI.updateProgressBar(self, (len(dataEmail))/i*100)
            print("Settings tab set")

        #catch out of bounds
        else:
            print("The given tab index was not found!")

        #general
        CreateUI.emailAddress = crypt.Encryption.decrypt(self, dab.DatabaseActions.read(self, table="configs", rows=1)[1][0])

    def updateProgressBar(self, value):
        prgWorking.setVisible(True)
        if value == 100:
            prgWorking.setValue(value)
            timer = QtCore.QTimer(self)
            timer.setSingleShot(True)
            timer.setInterval(1000)
            timer.timeout.connect(lambda:prgWorking.setVisible(False))
            timer.start()
        else:
            prgWorking.setValue(value)


        timer = QtCore.QTimer(self)
        timer.setSingleShot(True)
        timer.setInterval(500)
        timer.timeout.connect(lambda:CreateUI.updateProgressBar(self, 100))
        timer.start()

    def switchTab(self, tabIndex):
        CreateUI.setData(self, tabIndex)
        self.sCentral.setCurrentIndex(tabIndex)


    #PasswordsName, email, Username, Password, 2fa, category, banner
    def addPassword(self, passName, emailAdd, theUsername, thePassword, generated, twoFAEnabled, theCategory, theBanner, theComment):
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

    def clearData(self):
        lePassName.setText("")
        leUsername.setText("")
        leNewPass.setText("")
        chkGen.setChecked(False)
        chkTwoFA.setChecked(False)
        pteComment.setText("")

    def minimize(self):
        self.showMinimized()


    def mousePressEvent(self, event):
        global dragging
        global clickPos
        clickPos = event.pos()
        if clickPos.y() < 121:
            self.showNormal()
        if event.buttons() == QtCore.Qt.LeftButton:
            dragging = True

    def mouseReleaseEvent(self, event):
        global dragging
        dragging = False
        posit = self.pos()
        if posit.y() < 15:
            self.maximize()

    def mouseMoveEvent(self, event):
        global dragging
        global clickPos
        if dragging and clickPos.y() < 121:
            self.move(self.pos() + (event.pos() - clickPos))