from PyQt5 import QtGui, QtCore, QtWidgets
import seperator, dab, create
import qtawesome as qta

class CreateUI(QtWidgets.QWidget):
    def setup(self, passIndex, name, lastChanged, generated, password, banner="", email="", username="", category="generic", twoFa="False"):
        #Main layouts and layout widgets
        lMain = QtWidgets.QGridLayout()
        lMain.setContentsMargins(0,0,0,0)
        gMain = QtWidgets.QGridLayout()
        gMain.setContentsMargins(10,10,10,10)
        lMain.addLayout(gMain, 1, 0)
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

        #There is a layout (lmain) which holds the banner and the delete button so the delet btn can be directly in the corner
        iBanner.setPixmap(QtGui.QPixmap("./resources/icons/icon256.png").scaled(128, 128, QtCore.Qt.KeepAspectRatio))
        lMain.addWidget(iBanner, 0, 0)
        
        vQuit = QtWidgets.QVBoxLayout()
        vQuit.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        vQuit.setContentsMargins(0,0,0,0)
        btnDel = QtWidgets.QPushButton(qta.icon("fa.times", color="#f9f9f9"), "")
        btnDel.setObjectName("quitBtn")
        btnDel.setMinimumSize(QtCore.QSize(30,30))
        vQuit.addWidget(btnDel)
        wQuit = QtWidgets.QWidget()
        wQuit.setLayout(vQuit)
        lMain.addWidget(wQuit, 0, 1)

        #Create the widgets to display the main data
        lPassIndexLabel = QtWidgets.QLabel("Index:")
        gMain.addWidget(lPassIndexLabel, 1, 0)
        lPassIndex = QtWidgets.QLabel(passIndex)
        gMain.addWidget(lPassIndex, 1, 1)

        lNameLabel = QtWidgets.QLabel("Name:")
        gMain.addWidget(lNameLabel, 2, 0)
        lName = QtWidgets.QLabel(name)
        gMain.addWidget(lName, 2, 1)

        if email != "":
            lEmailLabel = QtWidgets.QLabel("Email:")
            gMain.addWidget(lEmailLabel, 3, 0)
            lEmail = QtWidgets.QLabel("")
            lEmail.setText(email)
            gMain.addWidget(lEmail, 3, 1)

        if username != "":
            lUsernameLabel = QtWidgets.QLabel("Email:")
            gMain.addWidget(lUsernameLabel, 4, 0)
            lUsername = QtWidgets.QLabel("")
            lUsername.setText(username)
            gMain.addWidget(lUsername, 4, 1)
        
        lPasswordLabel = QtWidgets.QLabel("Password:")
        gMain.addWidget(lPasswordLabel, 5, 0)
        lPassword = QtWidgets.QLabel(password)
        gMain.addWidget(lPassword, 5, 1)

        lCategoryLabel = QtWidgets.QLabel("Category")
        gMain.addWidget(lCategoryLabel, 6, 0)
        lCategory = QtWidgets.QLabel(str(category))
        gMain.addWidget(lCategory, 6, 1)

        lTwoFALabel = QtWidgets.QLabel("2FA")
        gMain.addWidget(lTwoFALabel, 7, 0)
        lTwoFA = QtWidgets.QLabel("2FA: ")
        if twoFa == "False":
            lTwoFA.setText("2FA: Inactive")
        elif twoFa == "True":
            lTwoFA.setText("2FA: Active")
        else:
            lTwoFA.setText("2FA: Error")
        gMain.addWidget(lTwoFA, 7, 1)

        lGeneratedLabel = QtWidgets.QLabel("Generated:")
        gMain.addWidget(lGeneratedLabel, 8, 0)
        lGenerated = QtWidgets.QLabel()
        if generated == "True":
            lGenerated.setText("True")
        elif generated == "False":
            lGenerated.setText("False")
        else:
            lGenerated.setText("Error")
        gMain.addWidget(lGenerated, 8, 1)

        lDateLabel = QtWidgets.QLabel("Last Changed:")
        gMain.addWidget(lDateLabel, 9, 0)       
        lDate = QtWidgets.QLabel(str(lastChanged).split(".")[0])
        gMain.addWidget(lDate, 9, 1)

        wMain.setLayout(lMain)
        vBack.addWidget(wMain)

        self.setLayout(vBack)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum))