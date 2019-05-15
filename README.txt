The question said that the server was low powered so I decided to fetch all tables and store them on my own system. Here are the steps to run the code for the queries (since the folder already has the csv, you can start from step 2). For the visualizations, I used the csv and imported them into Tableau. The two .twb files are the visualizations.

1. First 'read_data.py' to get all tables and store them as csv files
2. Run 'create_db.py' to create a new database on my own laptop (There's 'delete_db.py' if needed)
3. Run 'load_into_sql.py' to load the tables into the created database.
4. Run 'run_query.py' to get results of the questions. This will print only first 5 rows of each query by default. Run 'run_query.py 1' to print all rows.
