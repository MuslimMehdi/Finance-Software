import sqlite3
import sys

class Bank_Database():
    def __init__(self):
        self.connect = sqlite3.connect('bank.sqlite')
        self.cur = self.connect.cursor()
        self.command_init = '''CREATE TABLE IF NOT EXISTS User_Information(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            full_name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE,
            address TEXT NOT NULL,
            currency TEXT NOT NULL,
            balance REAL NOT NULL
        )'''
        self.cur.execute(self.command_init)
        self.connect.commit()#SQLite doesnt save until you commit
    def new_user(self, full_name, username, password, email, phone, address, currency, balance):
        self.cur.execute("INSERT INTO User_Information( full_name, username, password, email, phone, address, currency, balance) VALUES(?,?,?,?,?,?,?,?)")

        self.connect.commit()


b = Bank_Database()
