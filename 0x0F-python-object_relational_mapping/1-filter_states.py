#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa"""


import sys
import MYSQLdb

if __name__ = '__main__'
mydb = MYSQLdb.connect(
    host = "localhost",
    user = sys.argv[1],
    passward = sys.argv[2],
    port = 3306,
    db = sys.argv[3]
)

mycursor = mydb.cursor()

   cur.execute("SELECT states.id, name FROM states WHERE name "
                "COLLATE latin1_general_cs "
                "LIKE 'N%' "
                "ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
cursor.close()
db.close()