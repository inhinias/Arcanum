from PyQt5 import QtCore, QtWidgets
from components import crypt
import qtawesome as qta

class Generator(QtWidgets.QWidget):
    def __init__(self):
        super(Generator, self).__init__(flags=QtCore.Qt.FramelessWindowHint)
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("Generate Password")
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

        #How high all the widgets in the generator tab shoud be!
        height = 30

        #Generator tab layouts
        vMain = QtWidgets.QVBoxLayout()
        vMain.setAlignment(QtCore.Qt.AlignTop)

        gGeneratorMain = QtWidgets.QGridLayout()
        gGeneratorMain.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        vMain.addLayout(gGeneratorMain)

        #Generator widgets
        lLength = QtWidgets.QLabel("Length:")
        lLength.setMinimumHeight(height)
        gGeneratorMain.addWidget(lLength, 0, 0)

        sbLength = QtWidgets.QSpinBox()
        sbLength.setMinimum(8)
        sbLength.setValue(16)
        sbLength.setMaximum(128)
        gGeneratorMain.addWidget(sbLength, 0, 1)

        lSymbols = QtWidgets.QLabel("Include Symbols:")
        lSymbols.setMinimumHeight(height)
        gGeneratorMain.addWidget(lSymbols, 1, 0)

        chkSymbols = QtWidgets.QCheckBox("( e.g. @#$% )")
        gGeneratorMain.addWidget(chkSymbols, 1, 1)

        lNumbers = QtWidgets.QLabel("Include Numbers:")
        lNumbers.setMinimumHeight(height)
        gGeneratorMain.addWidget(lNumbers, 2, 0)

        chkNumbers = QtWidgets.QCheckBox("( e.g. 46872)")
        gGeneratorMain.addWidget(chkNumbers, 2, 1)
        
        lLowercase = QtWidgets.QLabel("Lowercase Letters:")
        lLowercase.setMinimumHeight(height)
        gGeneratorMain.addWidget(lLowercase, 3, 0)

        chkLowercase = QtWidgets.QCheckBox("( e.g. tpdnh )")
        gGeneratorMain.addWidget(chkLowercase, 3, 1)
        
        lUppercase = QtWidgets.QLabel("Uppercase Letters:")
        lUppercase.setMinimumHeight(height)
        gGeneratorMain.addWidget(lUppercase, 4, 0)

        chkUppercase = QtWidgets.QCheckBox("( e.g. IOERJDG )")
        gGeneratorMain.addWidget(chkUppercase, 4, 1)

        lAmbiguous = QtWidgets.QLabel("Symbols Without Ambiguous Characters:")
        lAmbiguous.setMinimumHeight(height)
        gGeneratorMain.addWidget(lAmbiguous, 5, 0)

        chkAmbiguous = QtWidgets.QCheckBox("(  { } [ ] ( ) / \ ' \" ` ~ , ; : . < > )")
        gGeneratorMain.addWidget(chkAmbiguous, 5, 1)

        btnGenerate = QtWidgets.QPushButton("Generate")
        btnGenerate.clicked.connect(lambda:Generator.generatePassword(self, sbLength.value(), 
            chkSymbols.isChecked(), chkNumbers.isChecked(), chkLowercase.isChecked(), chkUppercase.isChecked(), chkAmbiguous.isChecked()))
        gGeneratorMain.addWidget(btnGenerate, 6, 0)

        global lPassword
        lPassword = QtWidgets.QLabel("Password will be shown here!")
        lPassword.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        vMain.addWidget(lPassword)

        self.setLayout(vMain)
        self.show()

    def generatePassword(self, passLength, includeSymbols, includeNumbers, includeLowercase, includeUppercase, useAmbiguous):
        case = ""
        if includeLowercase and includeUppercase:
            case = "both"
        elif includeLowercase:
            case = "lowercase"
        elif includeUppercase:
            case = "uppercase"
        password = crypt.Encryption.genPassword(self, letters=case, 
            digits=includeNumbers, symbols=includeSymbols, safeSymbols=useAmbiguous, length=passLength)
        lPassword.setText(password)

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
    gui = Password()
    gui.show()
    app.exec_()