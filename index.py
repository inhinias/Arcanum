import sys, os, create, keyDialog
import qtawesome as qta
import create
from PyQt5 import QtGui, QtCore, QtWidgets

#This is the MAIN file of the app. Its used for handeling hte diffrent scripts within this programm.
#Debug prints are as formatted like this: FILE; CLASS; METHOD: MESSAGE

#Variables

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,1200,700)
        self.setWindowTitle("Axon")
        #self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint) #Use this for a frameless window. Will be used later!
        create.CreateUI.create(self)
        dial = keyDialog.CreateUI()
        dial.show()
        self.icon()

    def showMain(self):
        self.show()

    #Minimize and maximize methods for the new window action buttons
    def minimize(self):
        self.showMinimized()

    def maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def icon(self):
        #set app icon    
        app_icon = QtGui.QIcon()
        app_icon.addFile('icons/16x16.png', QtCore.QSize(16,16))
        app_icon.addFile('icons/32x32.png', QtCore.QSize(32,32))
        app_icon.addFile('icons/64x64.png', QtCore.QSize(64,64))
        app_icon.addFile('icons/128x128.png', QtCore.QSize(128,128))
        app_icon.addFile('icons/256x256.png', QtCore.QSize(256,256))
        app.setWindowIcon(app_icon)


if __name__ == '__main__':
    #Creating the QApplication
    app = QtWidgets.QApplication(sys.argv)

    #Set the main styling of the app
    with open("./stylesheet.css") as f:
        theme = f.read()
    app.setStyleSheet(theme)

    #Misc stuff
    window = Window()
    sys.exit(app.exec_())