#!/usr/bin/python3
"""
Lists all states with a name satsting with N from
the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
