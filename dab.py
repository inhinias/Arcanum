import os, create
import sqlite3 as dab
from PyQt5 import QtGui, QtCore, QtWidgets
from cryptography.fernet import Fernet

class Database:
    key = None
    db = None
    cur = None

    def create(self):
        Database.db = dab.connect("passwords.db")
        Database.cur = Database.db.cursor()
        Database.create_table(self)

    def create_table(self):
        Database.cur.execute('''CREATE TABLE IF NOT EXISTS PassTable(prim INTEGER PRIMARY KEY,place TEXT, crypt TEXT, info TEXT)''')
        Database.db.commit()

    def insert(self, place, crypt, info):
        try:
            f = Fernet(Database.key.encode())
        except:
            f = Fernet(Database.key)
        dataCrypt = [f.encrypt(place.encode()), f.encrypt(crypt.encode()), f.encrypt(info.encode())]
        Database.cur.execute("INSERT INTO PassTable(place, crypt, info) VALUES(?,?,?)", (dataCrypt[0], dataCrypt[1], dataCrypt[2]))
        Database.db.commit()

    def update(self, index, newPlace, newPass, newInfo):
        if newPlace != "":
            Database.cur.execute("UPDATE PassTable SET place = ? WHERE prim = ?", (newPlace, index))
            Database.db.commit()
        if newPlace != "":
            Database.cur.execute("UPDATE PassTable SET crypt = ? WHERE prim = ?", (newPass, index))
            Database.db.commit()
        if newPlace != "":
            Database.cur.execute("UPDATE PassTable SET info = ? WHERE prim = ?", (newInfo, index))
            Database.db.commit()
        create.CreateUI.populateList(self)

    def delete(self, prim):
        Database.cur.execute("DELETE FROM PassTable WHERE prim = ?", (prim,))
        Database.db.commit()
        create.CreateUI.populateList(self)

    def read(self, row):
        Database.cur.execute("SELECT *  FROM PassTable")
        return Database.cur.fetchall()[row]

    def length(self):
        Database.cur.execute("SELECT *  FROM PassTable")
        return len(Database.cur.fetchall())


    def createKey(self):
        Database.key = Fernet.generate_key()