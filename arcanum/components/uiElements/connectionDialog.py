import sys, index, logging, qtawesome as qta
from components import create, dab, crypt
from components.uiElements import crashDialog
from PyQt5 import QtGui, QtCore, QtWidgets

class CreateUI(QtWidgets.QWidget):
    #Create the dialog window for the connection data
    def __init__(self):
        super(CreateUI, self).__init__(flags=QtCore.Qt.FramelessWindowHint)
        self.setGeometry(50,50,450,100)
        self.setWindowTitle("Connect")
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.center()

        tbLay = QtWidgets.QHBoxLayout()
        tbLay.setAlignment(QtCore.Qt.AlignRight)
        tbLay.setContentsMargins(0,0,0,0)
        tbWid = QtWidgets.QWidget()
        tbWid.setObjectName("titlebar")
        tbWid.setLayout(tbLay)

        #Minimize button in the top left
        mini = QtWidgets.QPushButton(qta.icon("fa.minus", color="#f9f9f9"), "")
        mini.setObjectName("minimize")
        mini.setMinimumSize(QtCore.QSize(30,30))
        #mini.clicked.connect(CreateUI.minimize(self))
        tbLay.addWidget(mini)

        #Quit button in the top left
        quitBtn = QtWidgets.QPushButton(qta.icon("fa.times", color="#f9f9f9"), "")
        quitBtn.setObjectName("quitBtn")
        quitBtn.setMinimumSize(QtCore.QSize(30,30))
        quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        tbLay.addWidget(quitBtn)
        
        mainLay = QtWidgets.QVBoxLayout()
        mainLay.setContentsMargins(0,0,0,0)
        addressLay = QtWidgets.QGridLayout()
        mainLay.addWidget(tbWid)
        mainLay.addLayout(addressLay)

        #Connection details input
        #Note: the credentials here are just used for testing and not for real use!
        leHostname = QtWidgets.QLineEdit("kennethmathis.ch")
        leHostname.setPlaceholderText("Hostname")
        addressLay.addWidget(leHostname,0,0)

        lePort = QtWidgets.QLineEdit("3306")
        lePort.setValidator(QtGui.QIntValidator())
        lePort.setPlaceholderText("Port")
        addressLay.addWidget(lePort,0,1)

        leUsername = QtWidgets.QLineEdit("galenite")
        leUsername.setPlaceholderText("Username")
        mainLay.addWidget(leUsername)

        lePassword = QtWidgets.QLineEdit("pnR(z*j(xp85Sqf(")
        lePassword.setPlaceholderText("Password")
        lePassword.setEchoMode(2)
        mainLay.addWidget(lePassword)

        """
        leDatabase = QtWidgets.QLineEdit("passwords")
        leDatabase.setPlaceholderText("Database")
        mainLay.addWidget(leDatabase)
        """

        global leCryptPass
        leCryptPass = QtWidgets.QLineEdit("password")
        leCryptPass.setPlaceholderText("Encryption Password")
        leCryptPass.setEchoMode(2)
        mainLay.addWidget(leCryptPass)

        global lWrongPass
        lWrongPass = QtWidgets.QLabel("Wrong Password")
        lWrongPass.setObjectName("wrongPass")
        lWrongPass.setAlignment(QtCore.Qt.AlignHCenter)
        mainLay.addWidget(lWrongPass)
        lWrongPass.hide()

        btnConnect = QtWidgets.QPushButton("Connect")
        btnConnect.setObjectName("btnConnect")
        btnConnect.setMinimumHeight(38)
        btnConnect.clicked.connect(lambda:CreateUI.connect(
            self, username=leUsername.text(), thePassword=lePassword.text(), address=leHostname.text(), thePort=lePort.text(), theDatabase="passwords"))
        mainLay.addWidget(btnConnect)

        self.setLayout(mainLay)

    #Connect to the database and raise an error when failed
    def connect(self, username, thePassword, address, thePort, theDatabase):
        #Store the password in the encryption class as a global variable
        crypt.Encryption.password = leCryptPass.text()
        #Init the encryption class
        crypt.Encryption()

        #Connect to the database with the given data and test if we're connected.
        connectionStatus = dab.DatabaseActions.connect(self, username, thePassword, address, thePort, theDatabase)
        if connectionStatus == 0:
            #Test if the decryption password is correct. If not, show a text, that it is wrong.
            if CreateUI.testPassword(self, leCryptPass.text()):
                self.hide()
                index.Window.createMain(self)

            #The text about the wrong password here need to be replaced with a message dialog to make the message more clear.
            #This message dialog can be combined with error messages from the database connection. 
            else:
                logging.warning("Entered wrong decryption password")
                CreateUI.raiseError(self, "Wrong Decryption Password", "Password Error")
        
        #An error occured while connecting. This is what happend! N° 2 Will shock you! °-°
        elif connectionStatus == 1:
            CreateUI.raiseError(self, "Access to the DB denied. Wrong credentials?", "Database Connection Error")
            logging.warning("Access to the DB denied. Wrong credentials?")
        elif connectionStatus == 2:
            CreateUI.raiseError(self, "Bad DB error. Does the database exist?", "Database Connection Error")
            logging.warning("Bad DB error. Does the database exist?")
        else:
            logging.critical(connectionStatus)
            print(connectionStatus)
            #crashDialog(self, connectionStatus)

    #Show a message box giving more infromation about the current error
    def raiseError(self, errorMessage, title):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(str(errorMessage))
        msg.setWindowTitle(title)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = msg.exec_()

    #When connecting to the database this metho is called to test the given decrypting password.
    #The given password is used to decrypt the decryptTest from the config table. If this fails the given password is wrong.
    def testPassword(self, password):
        passTest = crypt.Encryption.decrypt(self, theData=dab.DatabaseActions.read(self, "configs", False, 0)[2])

        print(passTest)
        if passTest[0] != "":
            if passTest[1]: return True
            else: return False

    #Centers the window at the start
    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
    
    #When the connect dialog is closed quit the app
    def closeEvent(self, event):
        quit()

    #Method for minimizing the dialog
    def minimize(self):
        self.showMinimized()

    #Methods for moving the window with a custom titlebar
    def mousePressEvent(self, event):
        global dragging
        global clickPos
        clickPos = event.pos()
        if event.buttons() == QtCore.Qt.LeftButton:
            dragging = True

    def mouseReleaseEvent(self, event):
        global dragging
        dragging = False

    def mouseMoveEvent(self, event):
        global dragging
        global clickPos
        if dragging and clickPos.y() < 121:
            self.move(self.pos() + (event.pos() - clickPos))

#For executing this file standalone
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = CreateUI()
    gui.show()
    app.exec_()