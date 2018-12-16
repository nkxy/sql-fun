#!/usr/bin/env python3

import sqlite3
import random
import time
import datetime


class Person:
    def __init__(self, name, age, wish_list):
        self.name = name
        self.age = age
        self.wish_list = wish_list


conn = sqlite3.connect('database.db')
c = conn.cursor()
participants = [Person('Casey', 19, 'candles'),
                Person('Nick', 19, 'candy cane'),
                Person('Jason', 19, 'hype beast clothes'),
                Person('Sophie', 19, 'air pods')]


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS person(person_pk INTEGER PRIMARY KEY, name TEXT, age INTEGER, wish_list TEXT, date_created TEXT)')
    c.execute(
        'CREATE TABLE IF NOT EXISTS pairing(to_person_fk INTEGER,from_person_fk INTEGER)')


def add_casey():
    c.execute("INSERT INTO people VALUES('Casey Niu', 19)")
    conn.commit()


def add_nick():
    c.execute("INSERT INTO people VALUES('Nick Yang', 19)")
    conn.commit()


def close():
    c.close()
    conn.close()


def add_person(person):
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(
        unix).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute('INSERT INTO person (name, age, wish_list, date_created) VALUES(?, ?, ?, ?)',
              (person.name, person.age, person.wish_list, date))
    conn.commit()


def add_participants(participants):
    for person in participants:
        add_person(person)


create_table()
add_participants(participants)
close()
