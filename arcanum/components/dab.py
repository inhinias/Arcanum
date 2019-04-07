import datetime
import mysql.connector as connector
from components import create, crypt
from components.uiElements import connectionDialog
from PyQt5 import QtGui, QtCore, QtWidgets

#This is the main file for all database stuff connections and all SQL is handled within this file.

class DatabaseActions():
    #Connect to the database with the information given from the connectionDialog
    #Create all the necessary tables if needed
    def connect(self, username, thePassword, address, thePort=3306, theDatabase="passwords"):
        success = False
        try:
            global connection 
            connection = connector.connect(user=username, host=address, password=thePassword, port=int(thePort), database=theDatabase, buffered=True)
            print("Connection established!")
            global cur 
            cur = connection.cursor()

        #Catch any error and retrn them to the connection dialog to dislpay
        except connector.Error as err:
            if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Access to the DB denied. Wrong credentials?")
                return "Access to the DB denied. Wrong credentials?"
            elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
                print("Bad DB error. Does the database exist?")
                return "Bad DB error. Does the database exist?"
            else:
                print(err)
            return err
        
        #Return true if no error occurred otherwise the error code will be returned
        else: return True

    def createTables(self, databaseName):
        #Define a tables dictionary. The table name 
        tables = {}
        tables['passTable'] = (
            "CREATE TABLE IF NOT EXISTS " + databaseName + ".passTable("
            "prim int(11) PRIMARY KEY,"
            #Where the password is from
            "`name` VARCHAR(300),"
            #An email address with the account
            "email VARCHAR(300),"
            #The username to the password
            "username VARCHAR(300),"
            #When the password got last decrypted
            "lastUsed VARCHAR(300),"
            #If the pw got generated
            "generated VARCHAR(300),"
            #Is two factor authentication enabled
            "twoFA VARCHAR(300),"
            #The password in its encrypted form
            "encryptedPassword VARCHAR(300),"
            #Got anything to add? Put it here!
            "`comment` VARCHAR(300));"
        )
        tables['configs'] = (
            "CREATE TABLE IF NOT EXISTS " + databaseName + ".configs("
            "prim int(11) PRIMARY KEY,"
            #The standard email address. Further addresses are added in the rows after with the rest set to NULL.
            "emailAddress VARCHAR(300),"
            #This will be set at the first launch and used to test  if password/keys are correct.
            "decryptTest VARCHAR(300),"
            #How strong the asymmetic key length shold be
            "keyLength 4096,"
            #The last time the config got changed
            "lastChanged VARCHAR(300));"
        )

        #For RSA encryption to maybe speed up the de/encryption process.
        """
        tables['keys'] = (
            "CREATE TABLE IF NOT EXISTS " + databaseName + ".keys("
            "prim int(11) PRIMARY KEY,"
            #They keys value
            "key VARCHAR(600),"
            #How strong the key is
            "keyLength 4096,"
            #When the key got changed
            "lastRotation VARCHAR(300)),"
            #0=None, 1=AES256, 2=RSA
            #Pub Key arent encrypted, Private keys are either AES or RSA encrypted.
            "encryption INT"
        )
        """

        #Create all the tables
        for table_name in tables:
            table_description = tables[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                cur.execute(table_description)
            except connector.Error as err:
                if err.errno == connector.errorcode.ER_TABLE_EXISTS_ERROR:
                    print("The wanted table already exists.")
                else:
                    print(err.msg)
        print("All tables were create/exist!")

    #Close the connection to the database and its cursor object
    def closeEverything(self):
        cur.close()
        connection.close()

    #Returns the length of a given table
    #The wanted table gets determined with an if statment comparing the given table name string to a predetermined one here.
    #This way of sieving out table names needs more lines but adds mor flexibilty for diffrent tables.
    #It helps also to have less work with the database and keep everything in python.
    def getAmmount(self, table):
        ammount = 0
        if table=="passwords":
            cur.execute("SELECT COUNT(*) FROM passwords.passTable")
            try:
                ammount = cur.fetchall()[0][0]
            except:
                ammount = 0

        elif table=="configs":
            cur.execute("SELECT COUNT(*) FROM passwords.configs")
            ammount = cur.fetchall()[0][0]

        #The given table was not found, return nothing.
        else:
            print("unable to find table to get ammount of!")
            ammount = None

        return ammount
    
    #Read a table from the database
    #If everything from the table is wanted: everything=True
    #Else the wanted row needs to be given
    def read(self, table, everything=False, rows=1):
        #Test if everything is wanted and return the according table
        if everything:
            print("Getting the everything from {0}".format(table))
            dictOfRow = {'theRow':rows}
            if table == "passTable":
                cur.execute("SELECT * FROM passwords.passTable")
                return cur.fetchall()
            if table == "configs":
                cur.execute("SELECT * FROM passwords.configs")
                return cur.fetchall()

        #A row is wanted! Return the wanted one from the table
        else:
            if rows > 0:
                print("Getting row: {0} from table: {1}".format(rows, table))
                dictOfRow = {'theRow':rows}
                if table == "passTable":
                    cur.execute("SELECT * FROM passwords.passTable WHERE prim = %(theRow)s", dictOfRow)
                    return cur.fetchall()[0]
                if table == "configs":
                    cur.execute("SELECT * FROM passwords.configs WHERE prim = %(theRow)s", dictOfRow)
                    return cur.fetchall()[0]

    #Insert data into the database
    def insert(self, table, context):
        #PasswordsName, email, Username, Password, 2fa
        if table == "passwords":
            print("Inserting password")
            cur.execute("INSERT INTO passwords.passTable"
            "(name, email, username, category, lastUsed, generated, twoFA, encryptedPassword)"
            "VALUES (%(name)s, %(email)s, %(uName)s, %(lstUsed)s, %(gen)s, %(twofactor)s, %(crypticPass)s)", context)
            connection.commit()
        
        elif table == "configs":
            print("Inserting config")
            cur.execute("INSERT INTO passwords.configs"
            "(emailAddress, decryptTest, standardKeyLength, lastChanged)"
            "VALUES (%(email)s, %(passTest)s, %(keyLen)s, %(lstChanged)s)", context)
            connection.commit()
        
        #The wanted table wasnt found. Doing nothing!
        else:
            print("Table not found!")

    #Search for all the empty fields in the database
    def emptyDataTest(self):
        print("Testing password table")
        cur.execute("SELECT * FROM passwords.passTable")
        data = cur.fetchall()
        print(data)
    
    #Update a row in the given table
    def update(self, table, context, row=0):
        #Atm there is only the passwords table, may be expanded further
        if table == "passwords":
            print("Updating password")
            cur.execute("UPDATE passwords.passTable "
            "SET name = %(name)s, email = %(email)s, username = %(uName)s, lastUsed = %(lstUsed)s, "
            "generated = %(gen)s, twoFA = %(twofactor)s, encryptedPassword = %(crypticPass)s"
            "WHERE prim = %(index)s", context)
            connection.commit()
        
        #Do nothing upon a false table given
        else:
            print("Invalid table name for deletion")

    #Delete a row in a given table
    def delete(self, table, row):
        thisRow = { "theRow":row}
        if table == "passwords":
            print("Removing row {0} from {1}".format(row, table))
            cur.execute("DELETE FROM passwords.passTable WHERE prim = %(theRow)s", thisRow)
        elif table == "configs":
            print("Removing row {0} from {1}".format(row, table))
            cur.execute("DELETE FROM passwords.passTable WHERE prim = %(theRow)s", thisRow)
        else:
            print("Invalid table name for deletion")
    
