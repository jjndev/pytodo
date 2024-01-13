from connect import *

def list_entries():
    dbCon.row_factory = sql.Row
    dbCursor = dbCon.cursor()
    dbCursor.execute(f"Select entry, progress_percent FROM todo_entries ORDER BY {dbEntryOrderSqlString}")
    allRecords = dbCursor.fetchall()

    print(f"Listing {len(allRecords)} todo entries:")

    i = 1
    for record in allRecords:
        print(f"| #{i} | {record['entry']:<64} ( {record['progress_percent']:>3}% )")
        i += 1

