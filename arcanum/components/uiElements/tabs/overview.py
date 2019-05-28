from PyQt5 import QtCore, QtWidgets
from components import dab
import logging

class Overview(QtWidgets.QWidget):
    def __init__(self):
        super(Overview, self).__init__()

        #Overview tab layouts
        main = QtWidgets.QVBoxLayout()
        main.setAlignment(QtCore.Qt.AlignHCenter)
        #main.setSpacing(10) Change later so the diffrent numbers have more distance in between but not the title text!

        tTitleNumPass = QtWidgets.QLabel("Passwords Stored:")

        global tNumPasswords
        tNumPasswords = QtWidgets.QLabel("000000")
        tNumPasswords.setObjectName("numPasswords")

        tTitleEmail = QtWidgets.QLabel("E-Mail Addresses:")

        global tNumEmail
        tNumEmail = QtWidgets.QLabel("000000")
        tNumEmail.setObjectName("numPasswords")

        main.addWidget(tTitleNumPass)
        main.addWidget(tNumPasswords)
        main.addWidget(tTitleEmail)
        main.addWidget(tNumEmail)

        self.setLayout(main)


    def setGeneralInfo(self):
        #CreateUI.updateProgressBar(self, 0)
        numPass = dab.DatabaseActions.getAmmount(self, "passwords")
        numMail = dab.DatabaseActions.getAmmount(self, "email")
        if numPass == 0: tNumPasswords.setText("000000")
        elif len(str(numPass)) >= 6: tNumPasswords.setText(str(numPass))
        elif len(str(numPass)) == 5: tNumPasswords.setText("0" + str(numPass))
        elif len(str(numPass)) == 4: tNumPasswords.setText("00" + str(numPass))
        elif len(str(numPass)) == 3: tNumPasswords.setText("000" + str(numPass))
        elif len(str(numPass)) == 2: tNumPasswords.setText("0000" + str(numPass))
        elif len(str(numPass))== 1: tNumPasswords.setText("00000" + str(numPass))
        else: logging.error("Cant determine current ammount of passwords.")

        if numPass == 0: tNumPasswords.setText("000000")
        elif len(str(numMail)) >= 6: tNumEmail.setText(str(numMail))
        elif len(str(numMail)) == 5: tNumEmail.setText("0" + str(numMail))
        elif len(str(numMail)) == 4: tNumEmail.setText("00" + str(numMail))
        elif len(str(numMail)) == 3: tNumEmail.setText("000" + str(numMail))
        elif len(str(numMail)) == 2: tNumEmail.setText("0000" + str(numMail))
        elif len(str(numMail))== 1: tNumEmail.setText("00000" + str(numMail))
        else: logging.error("Cant determine current ammount of email addresses.")

        logging.info("Overview data set")