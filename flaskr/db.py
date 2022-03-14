import sqlite3

DATABASE = 'database.db'

def creat_names_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS names (id int, name char)")
    con.close()