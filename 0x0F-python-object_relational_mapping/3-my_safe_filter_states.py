#!/usr/bin/python3
"""
This module takes in an argument and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])

    # create cursor to exec queries using SQL; match arg given
    cur = db.cursor()
    query = """SELECT *
            FROM states
            WHERE name=%s
            ORDER BY id ASC"""
    cur.execute(query, (argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    # clean up
    cur.close()
    db.close()
