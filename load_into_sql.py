import csv

import mysql.connector as mysql


db = mysql.connect(host='localhost',
    user='root',
    passwd='sublime13',
    db='mydb')

cursor = db.cursor()

tables = ["consumer","consumer_product","consumer_servicerequest","sold_plan"]
columns_list = [('ConsumerID', 'MobileNo', 'EmailID','IsActive','CreatedDate'),
           ('ConsumerProductID', 'ConsumerID', 'BrandID', 'ProductID', 'IMEI1', 'IMEI2', 'SerialNo', 'DateOfPurchase', 'WarrantyTill', 'IsActive', 'CreatedDate'),
           ('ConsumerServiceRequestID', 'Source', 'ConsumerID', 'ConsumerProductID', 'SoldPlanID', 'ServiceTypeID', 'Lat', 'Lng', 'Zipcode', 'Status', 'ScheduledDateTime', 'CreatedDate'),
           ('SoldPlanID', 'PlanID', 'PlanAmount', 'FulfillerID', 'ConsumerProductID', 'ConsumerID', 'DateOfPurchase', 'DateOfActivation', 'ValidityDate', 'Status', 'Source', 'CreatedDate')]

columns = ['(ConsumerID, MobileNo, EmailID, IsActive, CreatedDate)',
           '(ConsumerProductID, ConsumerID, BrandID, ProductID, IMEI1, IMEI2, SerialNo, DateOfPurchase, WarrantyTill, IsActive, CreatedDate)',
           '(ConsumerServiceRequestID, Source, ConsumerID, ConsumerProductID, SoldPlanID, ServiceTypeID, Lat, Lng, Zipcode, Status, ScheduledDateTime, CreatedDate)',
          '(SoldPlanID, PlanID, PlanAmount, FulfillerID, ConsumerProductID, ConsumerID, DateOfPurchase, DateOfActivation, ValidityDate, Status, Source, CreatedDate)']


create_list = ["CREATE TABLE consumer(ConsumerID bigint(20), MobileNo varchar(20), EmailID varchar(150), IsActive tinyint(1), CreatedDate datetime)",
               "CREATE TABLE consumer_product(ConsumerProductID bigint(20), ConsumerID bigint(20), BrandID bigint(20), ProductID bigint(20), IMEI1  varchar(50), IMEI2  varchar(50), SerialNo varchar(50), DateOfPurchase date, WarrantyTill date, IsActive tinyint(1), CreatedDate datetime)",
               "CREATE TABLE consumer_servicerequest(ConsumerServiceRequestID bigint(20), Source varchar(50), ConsumerID bigint(20), ConsumerProductID bigint(20), SoldPlanID bigint(20), ServiceTypeID bigint(20), Lat decimal(20,6), Lng decimal(20,6), Zipcode int(6), Status varchar(100), ScheduledDateTime datetime, CreatedDate datetime)",
               "CREATE TABLE sold_plan(SoldPlanID bigint(19), PlanID bigint(19), PlanAmount int(19), FulfillerID bigint(19), ConsumerProductID bigint(19), ConsumerID bigint(19), DateOfPurchase datetime, DateOfActivation datetime, ValidityDate datetime, Status tinyint(4), Source varchar(255), CreatedDate datetime)"]

for i in range(len(tables)):
    print('Dealing with {} table'.format(tables[i]))
    fp = open(tables[i] + '.csv', 'r')
    csv_data = csv.reader(fp)
    cursor.execute(create_list[i])
    for row in csv_data:
        value_rep = "%s, "*len(columns_list[i])
        value_rep = value_rep[:-2]
        cursor.execute("INSERT INTO " + tables[i] + columns[i] + " VALUES(" + value_rep + ")", row)
    db.commit()
cursor.close()
