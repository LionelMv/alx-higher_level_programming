#!/usr/bin/python3
"""
Returns states starting with 'N'
parameters given to script: username, password, database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3])

    # create cursor to exec queries using SQL; filter names starting with 'N'
    cur = db.cursor()
    cur.execute(
        """SELECT *
        FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY id ASC"""
    )
    rows = cur.fetchall()

    for row in rows:
        print(row)

    #  clean up
    cur.close()
    db.close()
