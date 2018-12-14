import os, datetime
import mysql.connector as connector
from components import create, crypt
from components.uiElements import connectionDialog
from PyQt5 import QtGui, QtCore, QtWidgets

#This is the main file for all database stuff connections and all SQL is handled within this file.

class DatabaseActions():
    #Connect to the database with the information given from the connectionDialog
    #Add table creation here!!!
    def connect(self, username, thePassword, address, thePort=3306, theDatabase="passwords"):
        success = False
        try:
            global connection 
            connection = connector.connect(user=username, host=address, password=thePassword, port=int(thePort), database=theDatabase, buffered=True)
            print("Connection established!")
            global cur 
            cur = connection.cursor()

            #Defina all the necessary tables
            tables = {}
            tables['passTable'] = (
                "CREATE TABLE IF NOT EXISTS passTable("
                "prim int(11) PRIMARY KEY"
                "name VARCHAR(300)"
                "email VARCHAR(300)"
                "username VARCHAR(300)"
                "category VARCHAR(300)"
                "lastUsed VARCHAR(300)"
                "generated VARCHAR(300)"
                "banner VARCHAR(300)"
                "twoFA VARCHAR(300)"
                "encryptedPassword VARCHAR(300)"
                "comment VARCHAR(300))"
            )
            tables['configs'] = (
                "CREATE TABLE IF NOT EXISTS configs("
                "prim int(11) PRIMARY KEY"
                "configName VARCHAR(300)"
                "emailAddress VARCHAR(300)"
                "decryptTest VARCHAR(300)"
                "standarsKeyLength VARCHAR(300)"
                "lastChanged VARCHAR(300))"
            )
            tables['categories'] = (
                "CREATE TABLE IF NOT EXISTS categories("
                "prim int(11) PRIMARY KEY"
                "name VARCHAR(300)"
                "icon VARCHAR(300))"
            )
            tables['banners'] = (
                "CREATE TABLE IF NOT EXISTS passTable("
                "prim int(11) PRIMARY KEY"
                "name VARCHAR(300)"
                "path VARCHAR(300))"
            )

            #Create all the tables
            for table_name in tables:
                table_description = tables[table_name]
                try:
                    print("Creating table {}: ".format(table_name), end='')
                    cur.execute(table_description)
                except connector.Error as err:
                    if err.errno == connector.errorcode.ER_TABLE_EXISTS_ERROR:
                        print("already exists.")
                    else:
                        print(err.msg)
                else:
                    print("OK")

            #Report success
            success = True

        #Catch any error    
        except connector.Error as err:
            if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Access denied, wrong credentials?")
            elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
                print("Database not found!")
            else:
                print(err)
            print("Unable to connect")
        return success

    #Close the connection and the cursor
    def closeEverything(self):
        cur.close()
        connection.close()

    #Returns the length of a given table
    def getAmmount(self, table):
        ammount = 0
        if table=="passwords":
            cur.execute("SELECT COUNT(*) FROM passwords.passTable")
            try:
                ammount = cur.fetchall()[0][0]
            except:
                ammount = 0

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

        elif table=="configs":
            cur.execute("SELECT COUNT(*) FROM passwords.configs")
            ammount = cur.fetchall()[0][0]
            
            #Populate the config if no data is present
            if ammount == 0:
                print("THIS SHOULDNT BE ACTIVE WHEN THERE IS ALREADY SOMETHING IN IT!")
                rand = crypt.Encryption.encrypt(self, theData=crypt.Encryption.genPassword(self, True, True, length=16))
                name = crypt.Encryption.encrypt(self, "Generic")
                email = crypt.Encryption.encrypt(self, "")
                keylen = crypt.Encryption.encrypt(self, "4096")
                data = {'randString':rand, 'name':name, 'emailAdd':email, 'keyLen':keylen}
                cur.execute("INSERT INTO passwords.configs (configName, emailAddress, decryptTest, standardKeyLength) VALUES (%(name)s, %(emailAdd)s, %(randString)s, %(keyLen)s)", data)
                connection.commit()
        else:
            print("unable to find table to get ammount of!")


        return ammount
    
    def read(self, table, everything=False, rows=1):
        #Test the demand and return the according row
        if everything:
            print("Getting the everything from {0}".format(table))
            dictOfRow = {'theRow':rows}
            if table == "passTable":
                cur.execute("SELECT * FROM passwords.passTable")
                return cur.fetchall()
            if table == "categories":
                cur.execute("SELECT * FROM passwords.categories")
                return cur.fetchall()
            if table == "banners":
                cur.execute("SELECT * FROM passwords.banners")
                return cur.fetchall()
            if table == "configs":
                cur.execute("SELECT * FROM passwords.configs")
                return cur.fetchall()

        else:
            if rows >= 0:
                print("Getting row: {0} from table: {1}".format(rows, table))
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
                if table == "configs":
                    cur.execute("SELECT * FROM passwords.configs WHERE prim = %(theRow)s", dictOfRow)
                    return cur.fetchall()[0]

    def insert(self, table, context):
        #insert stuff
        #PasswordsName, email, Username, Password, 2fa, category, banner
        if table == "passwords":
            print("Inserting password")
            cur.execute("INSERT INTO passwords.passTable"
            "(name, email, username, category, lastUsed, generated, banner, twoFA, encryptedPassword)"
            "VALUES (%(name)s, %(email)s, %(uName)s, %(cat)s, %(lstUsed)s, %(gen)s, %(ban)s, %(twofactor)s, %(crypticPass)s)", context)
            connection.commit()
        
        elif table == "configs":
            print("Inserting password")
            cur.execute("INSERT INTO passwords.configs"
            "(configName, emailAddress, decryptTest, standardKeyLength, lastChanged)"
            "VALUES (%(name)s, %(email)s, %(dTest)s, %(keyLen)s, %(lstChanged)s)", context)
            connection.commit()

        else:
            print("Table not found!")

    #Search for all the empty fields in the database
    def emptyDataTest(self):
        print("Testing password table")
        cur.execute("SELECT * FROM passwords.passTable")
        data = cur.fetchall()
        print(data)
    
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
    
