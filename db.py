import sqlite3

connection  = sqlite3.connect("database.db")
cursor      = connection.cursor()


addColumn = "ALTER TABLE blood ADD COLUMN date text(32)"

cursor.execute(addColumn)

#Query the SQLite master table

tableQuery = "select * from sqlite_master"

cursor.execute(tableQuery)

tableList = cursor.fetchall()

 

# Print the updated listed of tables after renaming the stud table

for table in tableList:

    print("Database Object Type: %s"%(table[0]))

    print("Name of the database object: %s"%(table[1]))

    print("Name of the table: %s"%(table[2]))

    print("Root page: %s"%(table[3]))

    print("SQL Statement: %s"%(table[4]))

 

# close the database connection

connection.close()