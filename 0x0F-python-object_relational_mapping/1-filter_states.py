#!/usr/bin/python3

"""
    A script that lists all states from the database hbtn_0e_0_usa
    starting with capital letter N
    Username, password and database names are given as user args
"""


import sys
from unicodedata import name
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
