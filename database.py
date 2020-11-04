import sqlite3

connection = sqlite3.connect("akun.db")

cursor = connection.cursor()

command1 = """
CREATE TABLE IF NOT EXISTS akun(id INTEGER PRIMARY KEY, email TEXT type_UNIQUE, password TEXT, nomor_telepon TEXT)
"""

cursor.execute(command1)