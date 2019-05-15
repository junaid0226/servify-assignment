import csv
import mysql.connector as mysql

db = mysql.connect(
    host = "52.66.79.237",
    port = "3306",
    user = "candidate",
    passwd = "asdfgh123",
    database = "servify_assignment"
)

cursor = db.cursor()

tables = ["consumer","consumer_product","consumer_servicerequest","sold_plan"]

for table in tables:
	query = "SELECT * FROM " + table
	cursor.execute(query)
	rows = cursor.fetchall()
	fp = open(table + ".csv", "w")
	myFile = csv.writer(fp)
	myFile.writerows(rows)
	fp.close()