import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS people(name TEXT, age REAL)')


def add_casey():
    c.execute("INSERT INTO people VALUES('Casey Niu', 19)")
    conn.commit()


def add_nick():
    c.execute("INSERT INTO people VALUES('Nick Yang', 19)")
    conn.commit()


def close():
    c.close()
    conn.close()


create_table()
add_nick()
close()
