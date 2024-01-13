from connect import *

def update_entry_completion_percent(id, percent):
    if ( percent > 100 or percent < 0):
        print("Update was unsuccessful: Please enter a completion percent between 0 and 100.")
    
    percent = str(percent)

    dbCursor.execute(f"UPDATE todo_entries SET progress_percent = {percent} WHERE id = {id}")
    dbCon.commit()

    match percent:
        case 0:
            print("This entry has been marked as incomplete.")
        case 100:
            print("This entry has been marked as complete.")
        case _:
            print("This entry's progress percent has been updated.")

