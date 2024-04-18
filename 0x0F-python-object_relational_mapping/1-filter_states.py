#!/usr/bin/python3

"""
A script that lists all states from the database hbtn_0e_0_usa
starting with a capital letter N
Username, password, and database names are given as user args
"""

import sys
import MySQLdb

def main():
    """
    Main function to execute the script
    """

    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)


    try:
        db = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3],
                             host='localhost',
                             port=3306)
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM states \
                        WHERE name LIKE BINARY 'N%' \
                        ORDER BY id ASC")
    except MySQLdb.Error as e:
        print("Error executing SQL query:", e)
        cursor.close()
        db.close()
        sys.exit(1)

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()

if __name__ == '__main__':
    main()
