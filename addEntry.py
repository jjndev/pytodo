from connect import *

def add_entry():
    entry = input("Provide an entry to add to the list: (Max 64 Characters)")
    entryLength = len(entry)
    if entryLength > 64 or entryLength < 1:
        print("Entry was unsuccessful: please provide an entry between 1 and 64 characters.")
        return
    
    dbCursor.execute("INSERT INTO todo_entries (entry) VALUES(?)", (entry,))
    dbCon.commit()
    print("New entry successfully added.")
