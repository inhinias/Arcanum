from PyQt5 import QtCore, QtWidgets

class ErrorDialog():
    def __init__(self, errorMessage):
        super(ErrorDialog, self).__init__()
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(str(errorMessage))
        msg.setWindowTitle("uwu, Something went wrong!")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = msg.exec_()

        