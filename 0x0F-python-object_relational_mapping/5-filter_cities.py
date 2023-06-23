#!/usr/bin/python3

"""
This module lists all cities from given state name from the database.
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

    # create cursor to exec queries using SQL; join two tables for all info
    cur = db.cursor()
    cur.execute(
        """SELECT cities.name
        FROM states
        INNER JOIN cities ON states.id = cities.state_id
        WHERE states.name LIKE BINARY '{}'
        ORDER BY cities.id ASC""".format(argv[4])
    )

    cities = cur.fetchall()
    print(", ".join([city[0] for city in cities]))

    # clean up
    cur.close()
    db.close()
