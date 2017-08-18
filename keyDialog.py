import os, sys, dab, index, create
from PyQt5 import QtGui, QtCore, QtWidgets
from cryptography.fernet import Fernet

class CreateUI(QtWidgets.QWidget):
    keyExists = False
    msg = None
    def create(self):
        if not(os.path.isfile("./passwords.db")):
            dab.Database.createKey(self)
            return False
        else:
            return True
        
    def __init__(self):
        super(CreateUI, self).__init__()
        self.setGeometry(50,50,400,100)
        self.setWindowTitle("Axon")
        self.center()
        
        mainLay = QtWidgets.QVBoxLayout()

        infoText = QtWidgets.QLabel("")
        infoText.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        mainLay.addWidget(infoText)

        self.keyIn = QtWidgets.QLineEdit("")
        self.keyIn.setPlaceholderText("Place Key Here")
        self.keyIn.setVisible(False)
        mainLay.addWidget(self.keyIn)

        acceptBtn = QtWidgets.QPushButton("OK")
        acceptBtn.clicked.connect(lambda:CreateUI.accepted(self))
        mainLay.addWidget(acceptBtn)

        CreateUI.msg = QtWidgets.QMessageBox()

        self.setLayout(mainLay)

        if CreateUI.create(self):
            CreateUI.keyExists = True
            infoText.setVisible(False)
            self.keyIn.setVisible(True)
        
        else:
            infoText.setText("Key: {0}".format(str(dab.Database.key).lstrip("b")))

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
            
    def closeEvent(self, event):
        if not(CreateUI.keyJustAdded):
            quit()

    def accepted(self):
        if CreateUI.keyExists:
            try:
                dab.Database.key = self.keyIn.text()
                f = Fernet(dab.Database.key)
                f.decrypt(dab.Database.read(self, 0)[1])
                self.hide()
                create.CreateUI.populateList(self)

            except Exception:
                CreateUI.msg.setIcon(QtWidgets.QMessageBox.Information)
                CreateUI.msg.setText("Invalid Key")
                CreateUI.msg.setWindowTitle("Key Error")
                retval = CreateUI.msg.exec_()

        else:
            self.hide()
            create.CreateUI.populateList(self)

#For executing this file standalone
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = CreateUI()
    gui.show()
    app.exec_()