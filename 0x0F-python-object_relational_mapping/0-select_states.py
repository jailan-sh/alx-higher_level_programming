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
mycursor.excute("SELECT states.id FROM states ORDER BY states.id ASC")
row = cursor.fachall()
for state in row:
     print(state)
cursor.close()
db.close()