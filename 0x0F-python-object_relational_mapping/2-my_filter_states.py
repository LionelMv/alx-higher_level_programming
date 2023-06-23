#!/usr/bin/python3
"""
This module hat takes in an argument and
displays all values in the states table
of the database where name matches the argument.
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':

    # connect database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])

    # create cursor to execute SQL queries
    cur = db.cursor()
    cur.execute(
        """SELECT *
            FROM states
            WHERE name LIKE BINARY '{}'
            ORDER BY id ASC""".format(argv[4])
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    # clean up
    cur.close()
    db.close()
