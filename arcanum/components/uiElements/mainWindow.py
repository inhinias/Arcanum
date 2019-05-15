from PyQt5 import QtCore, QtWidgets, QtGui
from components import create
from components.uiElements.tabs import overview

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__(flags=QtCore.Qt.FramelessWindowHint)
        self.setGeometry(50,50,1320,700)
        self.setWindowTitle("Arcanum")
        create.CreateUI.create(self)
        self.center()
        self.show()
        create.CreateUI.setData(self, 0)
        overview.Overview.setGeneralInfo(self)

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

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