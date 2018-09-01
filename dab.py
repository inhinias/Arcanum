import os, create
import mysql.connector as connector
from PyQt5 import QtGui, QtCore, QtWidgets
from cryptography.fernet import Fernet

class DatabaseActions():
    def connect(self, username, thePassword, address, thePort=3306, theDatabase="passwords"):
        success = False
        try:
            global connection 
            connection = connector.connect(user=username, host=address, password=thePassword, port=int(thePort), database=theDatabase, buffered=True)
            print("Connection established!")
            global cur 
            cur = connection.cursor()
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

    def closeEverything(self):
        cur.close()
        connection.close()

    def getPasswordsAmmount(self):
        cur.execute("SELECT COUNT(*) FROM passwords.passTable")
        return cur.fetchall()[0][0]
    
    def read(self, table, rows):
        #Test the demand and return the according row
        if rows >= 0:
            print("getting row: {0} from table: {1}".format(rows, table))
            dictOfRow = {'theRow':rows}
            if table == "passTable":
                cur.execute("SELECT * FROM passwords.passTable WHERE prim = %(theRow)s", dictOfRow)
                return cur.fetchall()[0]

    def insert(self, table, row, context):
        #insert stuff
        print()
    
    def update(self, table, row, columns, context):
        #Change stuff
        print()

    def delete(self, table, row):
        #delete row
        print()
    
