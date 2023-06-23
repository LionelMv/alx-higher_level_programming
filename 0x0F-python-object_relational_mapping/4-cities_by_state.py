#!/usr/bin/python3

"""
This module lists all cities and their states from the database.
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
        """SELECT cities.id, cities.name, states.name
        FROM states
        INNER JOIN cities ON states.id = cities.state_id
        ORDER BY cities.id ASC"""
    )

    cities = cur.fetchall()
    for city in cities:
        print(city)

    cur.close()
    db.close()
