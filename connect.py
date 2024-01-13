import sqlite3 as sql

dbCon = sql.connect("./ToDoData.db")
# ./Projects\ToDoList\ToDoData.db")

dbCursor = dbCon.cursor()

dbEntryOrderSqlString = "datetime_updated ASC"

