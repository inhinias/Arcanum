import os, create, crypt, datetime
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

    def getAmmount(self, table):
        if table=="passwords":
            cur.execute("SELECT COUNT(*) FROM passwords.passTable")
            try:
                ammount = cur.fetchall()[0][0]
            except:
                ammount = 0
            return ammount
        elif table=="categories":
            cur.execute("SELECT COUNT(*) FROM passwords.categories")
            try:
                ammount = cur.fetchall()[0][0]
            except:
                ammount = 0
            return ammount
        else:
            print("unable to find table to get ammount of!")
    
    def read(self, table, rows):
        #Test the demand and return the according row
        if rows >= 0:
            print("getting row: {0} from table: {1}".format(rows, table))
            dictOfRow = {'theRow':rows}
            if table == "passTable":
                cur.execute("SELECT * FROM passwords.passTable WHERE prim = %(theRow)s", dictOfRow)
                return cur.fetchall()[0]
            if table == "categories":
                cur.execute("SELECT * FROM passwords.categories WHERE prim = %(theRow)s", dictOfRow)
                return cur.fetchall()[0]

    def insert(self, table, context):
        #insert stuff
        #PasswordsName, EMAS, Username, Password, 2fa, category, banner
        if table == "passwords":
            print("Inserting password")
            cur.execute("INSERT INTO passwords.passTable"
            "(name, email, username, category, lastUsed, generated, banner, twoFA, encryptedPassword)"
            "VALUES (%(name)s, %(email)s, %(uName)s, %(cat)s, %(lstUsed)s, %(gen)s, %(ban)s, %(twofactor)s, %(crypticPass)s)", context)

        else:
            print("Table not found!")
    
    def update(self, table, row, columns, context):
        #Change stuff
        print()

    def delete(self, table, row):
        #delete row
        print()
    
    def testPassword(self, password):
        #Should be finishable as soon as encrypted stuff is in the DB
        #crypt.Encryption()
        #dictOfRow = {'theRow':1}
        #cur.execute("SELECT * FROM passwords.passTable WHERE prim = %(theRow)s", dictOfRow)
        #firstPass = cur.fetchall()[0][9]
        #print(crypt.Encryption.decrypt(self, firstPass, password))
        return True
    
