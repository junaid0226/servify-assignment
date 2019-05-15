import sys
import mysql.connector as mysql

print_full = 0
if len(sys.argv) > 1:
	print_full = int(sys.argv[1])

db = mysql.connect(host='localhost',
    user='root',
    passwd='sublime13',
    db='mydb')

cursor = db.cursor(buffered=True)

query = "SELECT WEEK(DateOfPurchase) AS week, COUNT(*) AS total FROM sold_plan GROUP BY week ORDER BY week"
cursor.execute(query)
rows = cursor.fetchall()
print('*'*45)
print('Average no of plans sold per week')
print('*'*45)
print('(Week, Avg)')
print('-'*25)
if not print_full:
	rows = rows[:5]
for row in rows:
	print(row)
print('\n')

query = "SELECT cp.BrandID, COUNT(*) as counter FROM sold_plan AS sp INNER JOIN consumer_product AS cp ON sp.ConsumerProductID = cp.ConsumerProductID GROUP BY cp.BrandID ORDER BY counter DESC"
cursor.execute(query)
rows = cursor.fetchone()
print('*'*45)
print('Brand ID with the highest no of sold plans')
print('*'*45)
print('(Brand ID, Plans sold)')
print('-'*25)
print(rows)
print('\n')

query = "SELECT SoldPlanID as spi, COUNT(*) * 100.0 / (SELECT COUNT(*) from consumer_servicerequest) FROM consumer_servicerequest GROUP BY spi"
cursor.execute(query)
rows = cursor.fetchall()
print('*'*45)
print('Percentage of service requests for each plan')
print('*'*45)
print('(Plan ID, % requests)')
print('-'*25)
if not print_full:
	rows = rows[:5]
for row in rows:
	print(row)
print('\n')