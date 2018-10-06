import os, create, crypt, datetime, keyDialog
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
            ammount = cur.fetchall()[0][0]

            if ammount == 0:
                print("Adding Generic as a category")
                name = crypt.Encryption.encrypt(self, "Generic")
                path = crypt.Encryption.encrypt(self, "")
                catDict = {"name":name, "path":path}
                cur.execute("INSERT INTO passwords.categories (name, icon) VALUES (%(name)s, %(path)s)", catDict)
                connection.commit()
            return ammount

        elif table=="banners":
            cur.execute("SELECT COUNT(*) FROM passwords.banners")
            ammount = cur.fetchall()[0][0]
            if ammount == 0:
                print("Adding a basic banner")
                name = crypt.Encryption.encrypt(self, "Generic")
                path = crypt.Encryption.encrypt(self, "./resources/icons/icon256.png")
                banDict = {"name":name, "path":path}
                cur.execute("INSERT INTO passwords.banners (name, path) VALUES (%(name)s, %(path)s)", banDict)
                connection.commit()
            return ammount

        elif table=="configs":
            cur.execute("SELECT COUNT(*) FROM passwords.configs")
            ammount = cur.fetchall()[0][0]
            
            if ammount == 0:
                #The status updates for the progressbar are disabled due to issues i dont care atm to resolve
                #keyDialog.CreateUI.pEncStat.show()
                #keyDialog.CreateUI.pEncStat.setValue(0)
                rand = crypt.Encryption.encrypt(self, theData=crypt.Encryption.randString(self))
                #keyDialog.CreateUI.pEncStat.setValue(20)
                name = crypt.Encryption.encrypt(self, "Generic")
                #keyDialog.CreateUI.pEncStat.setValue(40)
                email = crypt.Encryption.encrypt(self, "")
                #keyDialog.CreateUI.pEncStat.setValue(60)
                keylen = crypt.Encryption.encrypt(self, "4096")
                #keyDialog.CreateUI.pEncStat.setValue(80)
                data = {'randString':rand, 'name':name, 'emailAdd':email, 'keyLen':keylen}
                cur.execute("INSERT INTO passwords.configs (configName, emailAddress, decryptTest, standardKeyLength) VALUES (%(name)s, %(emailAdd)s, %(randString)s, %(keyLen)s)", data)
                connection.commit()
                #keyDialog.CreateUI.pEncStat.setValue(100)
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
            if table == "banners":
                cur.execute("SELECT * FROM passwords.banners WHERE prim = %(theRow)s", dictOfRow)
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
    
    def testPassword(self, password, configRow=1):
        crypt.Encryption()
        passed = False
        length = DatabaseActions.getAmmount(self, "configs")
        if length > 0:
            dictOfRow = {'theRow':configRow}
            cur.execute("SELECT * FROM passwords.configs WHERE prim = %(theRow)s", dictOfRow)
            passTest = crypt.Encryption.decrypt(self, theData=cur.fetchall()[0][3])
            if passTest[1]:
                return True
            else:
                return False
        elif length == 0:
            return True
        else:
            print("Error parsing config length while testing the password!")
            return False
    
