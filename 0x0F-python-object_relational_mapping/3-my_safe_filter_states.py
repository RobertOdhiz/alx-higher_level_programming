#!/usr/bin/python3
"""
Script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa tables where name matches
the argument
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()

    sql = """ SELECT * FROM states
          WHERE name = %s
          ORDER BY id ASC """

    cur.execute(sql, (sys.argv[4],))

    data = cur.fetchall()

    for row in data:
        print(row)

    cur.close()
    db.close()
