#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == '__main__':
    mydb = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        port=3306,
        db=sys.argv[3]
    )
    mycursor = mydb.cursor()
    sql = "SELECT cities.id, name FROM cities\
           ORDER BY cities.id ASC"
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    for row in rows:
        print("({}, '{}', '{}')".format(row[0], row[1], row[2]))
    mycursor.close()
    mydb.close()
