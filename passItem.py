from PyQt5 import QtGui, QtCore, QtWidgets
import seperator, dab, create
import qtawesome as qta

class CreateUI(QtWidgets.QWidget):
    def setup(self, name, lastChanged, generated, password, banner="", email="", username="", category="generic", twoFa=False):
        #Main layouts and layout widgets
        vMain = QtWidgets.QVBoxLayout()
        wMain = QtWidgets.QWidget()
        wMain.setObjectName("passSlate")
        vBack = QtWidgets.QVBoxLayout()
        vBack.setContentsMargins(0,0,0,0)

        #Banner to the Password currently only in placeholder version!
        iBanner = QtWidgets.QLabel()
        """
        if banner != "":
            try:
                iBanner.setPixmap(QtGui.QPixmap(banner).scaled(256, 256, QtCore.Qt.KeepAspectRatio))
            except:
                iBanner.setPixmap(QtGui.QPixmap("./resources/icons/icon256.png").scaled(256, 256, QtCore.Qt.KeepAspectRatio))
        else:
            """

        iBanner.setPixmap(QtGui.QPixmap("./resources/icons/icon256.png").scaled(128, 128, QtCore.Qt.KeepAspectRatio))
        vMain.addWidget(iBanner)
        

        lName = QtWidgets.QLabel('Name: ' + name)
        vMain.addWidget(lName)

        if email != "":
            lEmail = QtWidgets.QLabel("")
            lEmail.setText('Email: ' + email)
            vMain.addWidget(lEmail)

        if username != "":
            lUsername = QtWidgets.QLabel("")
            lUsername.setText('Username: ' + username)
            vMain.addWidget(lUsername)

        lPassword = QtWidgets.QLabel('Password: ' + password)
        vMain.addWidget(lPassword)

        lCategory = QtWidgets.QLabel("Category: " + str(category))
        vMain.addWidget(lCategory)

        lTwoFA = QtWidgets.QLabel("2FA: ")
        if twoFa == 0:
            lTwoFA.setText("2FA: Inactive")
        elif twoFa == 1:
            lTwoFA.setText("2FA: Active")
        else:
            lTwoFA.setText("2FA: Error")
        vMain.addWidget(lTwoFA)

        lGenerated = QtWidgets.QLabel("")
        if generated:
            lGenerated.setText("Generated: True")
        else:
            lGenerated.setText("Generated: False")
        vMain.addWidget(lGenerated)

        lDate = QtWidgets.QLabel("Last Changed: " + str(lastChanged))
        vMain.addWidget(lDate)

        wMain.setLayout(vMain)
        vBack.addWidget(wMain)

        self.setLayout(vBack)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum))