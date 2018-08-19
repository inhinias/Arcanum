import os, create
import mysql.connector as connector
from PyQt5 import QtGui, QtCore, QtWidgets
from cryptography.fernet import Fernet

class DatabaseActions():
    def connect(self, username, thePassword, address, thePort=3306, theDatabase="passwords"):
        success = False
        try:
            connection = connector.connect(user=username, host=address, password=thePassword, port=int(thePort), database=theDatabase)
            print("Connection established and closed")
            connection.close()
            success = True
        except connector.Error as err:
            if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Access denied, wrong credentials?")
            elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
                print("Database not found!")
            else:
                print(err)
            print("Unable to connect")
        return success
    
    def read(self, table, rows):

        if rows == 0:
            #return everything
            print()
        else:
            #return all the rows
            print()

    def insert(self, table, row, context):
        #insert stuff
        print()
    
    def update(self, table, row, columns, context):
        #Change stuff
        print()

    def delete(self, table, row):
        #delete row
        print()
    
