#!/usr/bin/python3
"""
Script that takes in the name of the state as an argument and
lists all cities of that state
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

    query = """ SELECT c.name
            FROM states s
            INNER JOIN cities c ON s.id = c.state_id
            WHERE s.name = %s
            ORDER BY c.id ASC """

    cur.execute(query, (sys.argv[4],))

    data = cur.fetchall()

    print(", ".join([row[0] for row in data]))

    cur.close()
    db.close()
