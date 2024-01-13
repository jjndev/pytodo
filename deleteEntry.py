from connect import *

def delete_entry(id):
    dbCursor.execute(f"DELETE from todo_entries WHERE id = {id}")
    dbCon.commit()
    print("This entry has been deleted.")

