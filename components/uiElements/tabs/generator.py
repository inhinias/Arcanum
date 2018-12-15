from PyQt5 import QtCore, QtWidgets
from components import crypt

class Generator(QtWidgets.QWidget):
    def __init__(self):
        super(Generator, self).__init__()

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
        sbLength.setMaximum(120)
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

        lAmbiguous = QtWidgets.QLabel("Exclude Ambiguous Characters:")
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
        vMain.addWidget(lPassword)

        self.setLayout(vMain)

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