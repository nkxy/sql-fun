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
        'CREATE TABLE IF NOT EXISTS pairing(to_person_fk INTEGER, from_person_fk INTEGER, FOREIGN KEY (to_person_fk) REFERENCES person(person_pk), FOREIGN KEY (from_person_fk) REFERENCES person(person_pk))')


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


def add_pairing():
    arr = [1, 2, 3, 4]
    for x in range(len(participants)):
        to_person = x + 1
        from_person = random.choice(arr);
        while (from_person == to_person):
            from_person = random.choice(arr)
        arr.remove(from_person)
        c.execute('INSERT INTO pairing (to_person_fk, from_person_fk) VALUES(?, ?)', (to_person, from_person))

    conn.commit()


create_table()
add_pairing()
# add_participants(participants)
close()
