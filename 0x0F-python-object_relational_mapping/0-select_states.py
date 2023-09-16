#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == '__main__':
    mydb = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           port=3306,
                           db=sys.argv[3]
                           )
    mycursor = mydb.cursor()
    sql = "SELECT states.id, name FROM states ORDER BY states.id ASC"
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
mydb.close()