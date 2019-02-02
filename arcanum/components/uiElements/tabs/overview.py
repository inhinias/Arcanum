from PyQt5 import QtCore, QtWidgets
from components import dab

class Overview(QtWidgets.QWidget):
    def __init__(self):
        super(Overview, self).__init__()

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

        wOCenter = QtWidgets.QWidget()
        """wOCenter.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))"""
        wOCenter.setLayout(vOCenter)

        #Create the overview page
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

        statTexts = ["Reused","Lost","Generated","2FA","EMail","Leaked"]
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

        tLost = QtWidgets.QLabel("0")
        tLost.setObjectName("oText")
        gStats.addWidget(tLost,1,1)

        tGen = QtWidgets.QLabel("0")
        tGen.setObjectName("oText")
        gStats.addWidget(tGen,2,1)

        tTwoFA = QtWidgets.QLabel("0")
        tTwoFA.setObjectName("oText")
        gStats.addWidget(tTwoFA,3,1)

        tEmailAdresses = QtWidgets.QLabel(str(dab.DatabaseActions.getAmmount(self, "configs")-1))
        tEmailAdresses.setObjectName("oText")
        gStats.addWidget(tEmailAdresses,4,1)

        tLeaked = QtWidgets.QLabel("0")
        tLeaked.setObjectName("oText")
        gStats.addWidget(tLeaked,5,1)

        hOverview.addLayout(gStrength)
        hOverview.addWidget(wOCenter)
        hOverview.addLayout(gStats)

        dab.DatabaseActions.getAmmount(self, "banners")
        dab.DatabaseActions.getAmmount(self, "categories")

        self.setLayout(hOverview)
    
    def setNumPasswords(self, ammount):
        tNumPasswords.setText(str(ammount))