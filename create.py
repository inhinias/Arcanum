from PyQt5 import QtGui, QtCore, QtWidgets
from cryptography.fernet import Fernet
import qtawesome as qta
import dab, passItem

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
        #Layouts
        #Main Layouts
        vBack = QtWidgets.QVBoxLayout() #Backbone layout for color at the lowest level
        vBack.setContentsMargins(0,0,0,0)
        vMain = QtWidgets.QVBoxLayout() #Layouts for the main stuff
        hMain = QtWidgets.QHBoxLayout()
        vMain.setContentsMargins(0,0,0,0)
        hMain.setContentsMargins(5,0,5,5)
        vToolRack = QtWidgets.QVBoxLayout()
        vToolRack.setAlignment(QtCore.Qt.AlignTop)
        sCentral = QtWidgets.QStackedLayout()

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

        gPasswords = QtWidgets.QGridLayout()

        #Layout widgets
        wOverview = QtWidgets.QWidget()
        wOverview.setLayout(hOverview)
        sCentral.addWidget(wOverview)

        wOCenter = QtWidgets.QWidget()
        #wOCenter.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        wOCenter.setLayout(vOCenter)

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
        wCentral.setLayout(sCentral)
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
        #mini.clicked.connect(CreateUI.minimize(self))
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

        btnOverview.setMinimumHeight(rackBtnMinheight)
        btnPasswords.setMinimumHeight(rackBtnMinheight)
        btnGenerate.setMinimumHeight(rackBtnMinheight)
        btnNotes.setMinimumHeight(rackBtnMinheight)
        btnBunkers.setMinimumHeight(rackBtnMinheight)

        btnOverview.setIconSize(rackIcoSize)
        btnPasswords.setIconSize(rackIcoSize)
        btnGenerate.setIconSize(rackIcoSize)
        btnNotes.setIconSize(rackIcoSize)
        btnBunkers.setIconSize(rackIcoSize)

        vToolRack.addWidget(btnOverview)
        vToolRack.addWidget(btnPasswords)
        vToolRack.addWidget(btnGenerate)
        vToolRack.addWidget(btnNotes)
        vToolRack.addWidget(btnBunkers)

        #Create the overview page
        #Strength overview
        strengthLvls = ["Very Weak","Weak","Acceptable","Strong","Very Strong","Fort Knox"]
        for i in range(len(strengthLvls)):
            sLabel = QtWidgets.QLabel(strengthLvls[i] + ":")
            sLabel.setObjectName("oText")
            gStrength.addWidget(sLabel,i,0)
        
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
        tNumPasswords = QtWidgets.QLabel("00000")
        tNumPasswords.setObjectName("numPasswords")
        vOCenter.addWidget(tNumPasswords)

        statTexts = ["Reused","Forgotten","Generated","2FA","In RockYou","Leaked"]
        for j in range(len(statTexts)):
            sStats = QtWidgets.QLabel(statTexts[j] + ":")
            sStats.setObjectName("oText")
            gStats.addWidget(sStats,j,0)

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


        self.setLayout(vBack)

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