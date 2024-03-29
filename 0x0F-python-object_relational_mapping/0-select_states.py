#!/usr/bin/python3
import MySQLdb
import sys

if len(sys.argv) != 4:
    print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database
)

cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
results = cursor.fetchall()
for row in results:
    print("{}".format(row))

cursor.close()
db.close()
