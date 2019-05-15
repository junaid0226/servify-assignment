import mysql.connector as mysql
db = mysql.connect(host='localhost',
    user='root',
    passwd='sublime13',
    db='mydb')
cursor = db.cursor()
cursor.execute("DROP DATABASE mydb")