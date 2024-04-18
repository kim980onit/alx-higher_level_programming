#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

def print_n_states(username, password, database):
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
    else:
        print_n_states(argv[1], argv[2], argv[3])
