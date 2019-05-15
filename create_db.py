import mysql.connector as mysql
db = mysql.connect(host='localhost',
    user='root',
    passwd='sublime13')
cursor = db.cursor()
cursor.execute("CREATE DATABASE mydb")