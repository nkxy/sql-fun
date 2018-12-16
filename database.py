import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS people(name TEXT, age REAL)')


def add_casey():
    c.execute("INSERT INTO people VALUES('Casey Niu', 19)")
    conn.commit()
    conn.close()
    c.close()


create_table()
add_casey()
