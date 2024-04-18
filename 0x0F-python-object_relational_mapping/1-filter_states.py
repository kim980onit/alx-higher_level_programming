#!/usr/bin/python3
"""
Script to list all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.

Usage:
    python3 1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 1-filter_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()