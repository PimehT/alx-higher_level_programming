#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    db="hbtn_0e_0_usa"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
results = cursor.fetchall()
for row in results:
    print("{}".format(row))

cursor.close()
db.close()