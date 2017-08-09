import pickle, os, sys, MySQLdb, create, index
from PyQt5 import QtGui, QtCore, QtWidgets
from cryptography.fernet import Fernet

class CreateUI(QtWidgets.QWidget):
    keyJustAdded = False
    def create(self):
        keyGenerated = False
        if not(os.path.isfile("./data.txt")):
            keyGenerated = True
            create.CreateUI.createKey(self)
            file = open("data.txt", "w+")
            file.write("{0},{1}".format(keyGenerated, create.CreateUI.key))
            file.close()
            return False
        else:
            return True
        
    def __init__(self):
        super(CreateUI, self).__init__()
        self.setGeometry(50,50,400,100)
        self.setWindowTitle("Axon")
        
        mainLay = QtWidgets.QVBoxLayout()

        infoText = QtWidgets.QLabel("LLLLL")
        mainLay.addWidget(infoText)

        self.keyIn = QtWidgets.QLineEdit("Place Key Here")
        self.keyIn.setVisible(False)
        mainLay.addWidget(self.keyIn)

        acceptBtn = QtWidgets.QPushButton("OK")
        acceptBtn.clicked.connect(lambda:CreateUI.accepted(self))
        mainLay.addWidget(acceptBtn)

        self.setLayout(mainLay)

        if CreateUI.create(self):
            CreateUI.keyJustAdded = True
            infoText.setVisible(False)
            self.keyIn.setVisible(True)
        
        else:
            dataIn = open("./data.txt", "r")
            dataText = dataIn.read()
            print(dataText)
            infoText.setText("Key: {0}".format(create.CreateUI.key))
            
    def closeEvent(self, event):
        if not(CreateUI.keyJustAdded):
            quit()

    def accepted(self):
        if CreateUI.keyJustAdded:
            self.hide()
            index.Window.showMain()
        else:
            create.CreateUI.key = self.keyIn.text()
            self.hide()
            index.window.showMain()

#For executing this file standalone
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = CreateUI()
    gui.show()
    app.exec_()