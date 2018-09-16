import sys, os, create, keyDialog
import qtawesome as qta
import create
from PyQt5 import QtGui, QtCore, QtWidgets

#This is the MAIN file of the app. Its used for handeling hte diffrent scripts within this programm.
#Debug prints are as formatted like this: FILE; CLASS; METHOD: MESSAGE

#Variables

class Window(QtWidgets.QWidget):
    #Global stuff (none I guess?!)

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,1320,700)
        self.setWindowTitle("Arcanum")
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint) #Use this for a frameless window. Will be used later!
        dial = keyDialog.CreateUI()
        #dab.Database.create(self)
        create.CreateUI.create(self)
        self.icon()
        self.show()
        dial.show()
        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    #set the application icon
    def icon(self):    
        app_icon = QtGui.QIcon()
        app_icon.addFile('./resources/icons/icon16.png', QtCore.QSize(16,16))
        app_icon.addFile('./resources/icons/icon32.png', QtCore.QSize(32,32))
        app_icon.addFile('./resources/icons/icon64.png', QtCore.QSize(64,64))
        app_icon.addFile('./resources/icons/icon128.png', QtCore.QSize(128,128))
        app_icon.addFile('./resources/icons/icon256.png', QtCore.QSize(256,256))
        app.setWindowIcon(app_icon)

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

"""

          _____                    _____                    _____                    _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \                /::\    \                /::\____\                /::\____\                /::\____\        
       /::::\    \              /::::\    \              /::::\    \              /::::\    \              /::::|   |               /:::/    /               /::::|   |        
      /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \            /:::::|   |              /:::/    /               /:::::|   |        
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /::::::|   |             /:::/    /               /::::::|   |        
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/  \:::\    \        /:::/__\:::\    \        /:::/|::|   |            /:::/    /               /:::/|::|   |        
   /::::\   \:::\    \      /::::\   \:::\    \      /:::/    \:::\    \      /::::\   \:::\    \      /:::/ |::|   |           /:::/    /               /:::/ |::|   |        
  /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/    / \:::\    \    /::::::\   \:::\    \    /:::/  |::|   | _____    /:::/    /      _____    /:::/  |::|___|______  
 /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\  /:::/    /   \:::\    \  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \  /:::/____/      /\    \  /:::/   |::::::::\    \ 
/:::/  \:::\   \:::\____\/:::/  \:::\   \:::|    |/:::/____/     \:::\____\/:::/  \:::\   \:::\____\/:: /    |::|   /::\____\|:::|    /      /::\____\/:::/    |:::::::::\____\
\::/    \:::\  /:::/    /\::/   |::::\  /:::|____|\:::\    \      \::/    /\::/    \:::\  /:::/    /\::/    /|::|  /:::/    /|:::|____\     /:::/    /\::/    / ~~~~~/:::/    /
 \/____/ \:::\/:::/    /  \/____|:::::\/:::/    /  \:::\    \      \/____/  \/____/ \:::\/:::/    /  \/____/ |::| /:::/    /  \:::\    \   /:::/    /  \/____/      /:::/    / 
          \::::::/    /         |:::::::::/    /    \:::\    \                       \::::::/    /           |::|/:::/    /    \:::\    \ /:::/    /               /:::/    /  
           \::::/    /          |::|\::::/    /      \:::\    \                       \::::/    /            |::::::/    /      \:::\    /:::/    /               /:::/    /   
           /:::/    /           |::| \::/____/        \:::\    \                      /:::/    /             |:::::/    /        \:::\__/:::/    /               /:::/    /    
          /:::/    /            |::|  ~|               \:::\    \                    /:::/    /              |::::/    /          \::::::::/    /               /:::/    /     
         /:::/    /             |::|   |                \:::\    \                  /:::/    /               /:::/    /            \::::::/    /               /:::/    /      
        /:::/    /              \::|   |                 \:::\____\                /:::/    /               /:::/    /              \::::/    /               /:::/    /       
        \::/    /                \:|   |                  \::/    /                \::/    /                \::/    /                \::/____/                \::/    /        
         \/____/                  \|___|                   \/____/                  \/____/                  \/____/                  ~~                       \/____/         
                                                                                                                                                                               
"""
