import os, MySQLdb
from PyQt5 import QtGui, QtCore, QtWidgets
from cryptography.fernet import Fernet

class CreateUI:
    key = ""

    def create(self):
        print("ö")

    def createKey(self):
        CreateUI.key = Fernet.generate_key()