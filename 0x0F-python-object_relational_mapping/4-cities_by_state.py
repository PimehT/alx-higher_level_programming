#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
Results must be sorted in ascending order by cities.id
"""
import MySQLdb
import sys

if len(sys.argv) != 4:
    err_msg = "Usage: {} <username> <password> <database>"
    print(err_msg.format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database,
    charset="utf8"
)

cursor = db.cursor()
query = "SELECT cities.id, cities.name AS city_name, states.name AS state_name"
query += " FROM cities"
query += " JOIN states ON cities.state_id = states.id"
query += " ORDER BY cities.id ASC"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print("{}".format(row))

cursor.close()
db.close()
