from PyQt5 import QtCore, QtWidgets
from components import dab

class Overview(QtWidgets.QWidget):
    def __init__(self):
        super(Overview, self).__init__()

        #Overview tab layouts
        main = QtWidgets.QVBoxLayout()
        main.setAlignment(QtCore.Qt.AlignHCenter)

        tTitleNumPass = QtWidgets.QLabel("Passwords Stored:")

        global tNumPasswords
        tNumPasswords = QtWidgets.QLabel("000000")
        tNumPasswords.setObjectName("numPasswords")

        main.addWidget(tTitleNumPass)
        main.addWidget(tNumPasswords)

        self.setLayout(main)


    def setGeneralInfo(self):
        #CreateUI.updateProgressBar(self, 0)
        numPass = dab.DatabaseActions.getAmmount(self, "passwords")
        print("Currently {0} passwords stored".format(numPass))
        #CreateUI.updateProgressBar(self, 50)
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
            logging.error("Cant determine current ammount of passwords.")

        print("Overview data set")