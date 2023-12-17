#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
from the database
"""
import sys
import MySQLdb


if __name__ = '__main__':
    db = mySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states\
                WHERE name LIKE BINARY 'N%'\
                ORDER BY id ASC")

    data = cursor.fetchall()

    for row in data:
        print(row)

    cur.close()
    db.close()
