#!/usr/bin/python3
"""
List all states with the 'search name given' from the table states
in the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if len(sys.argv) != 5:
    err_msg = "Usage: {} <username> <password> <database> <name>"
    print(err_msg.format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
st_name = sys.argv[4]

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database
)

cursor = db.cursor()
query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
cursor.execute(query, (st_name,))
results = cursor.fetchall()
for row in results:
    print("{}".format(row))

cursor.close()
db.close()
