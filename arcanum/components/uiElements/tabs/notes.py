from PyQt5 import QtCore, QtWidgets

class Notes(QtWidgets.QWidget):
    def __init__(self):
        super(Notes, self).__init__()
        
        #Notes tab layouts
        hNotesMain = QtWidgets.QHBoxLayout()
        hNotesMain.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)

        hCreateNote = QtWidgets.QHBoxLayout()
        hCreateNote.setAlignment(QtCore.Qt.AlignTop)
        hCreateNote.setSpacing(10)
        hNotesMain.addLayout(hCreateNote)

        self.setLayout(hNotesMain)