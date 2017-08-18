import os
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
        f = Fernet(Database.key.encode())
        dataCrypt = [f.encrypt(place.encode()), f.encrypt(crypt.encode()), f.encrypt(info.encode())]
        Database.cur.execute("INSERT INTO PassTable(place, crypt, info) VALUES(?,?,?)", (dataCrypt[0], dataCrypt[1], dataCrypt[2]))
        Database.db.commit()

    def update(self, index, newCrypt):
        print("R")

    def delete(self, index):
        print("R")

    def read(self, row):
        Database.cur.execute("SELECT *  FROM PassTable")
        return Database.cur.fetchall()[row]

    def length(self):
        Database.cur.execute("SELECT *  FROM PassTable")
        return len(Database.cur.fetchall())


    def createKey(self):
        Database.key = Fernet.generate_key()