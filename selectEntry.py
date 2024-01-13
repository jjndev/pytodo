from connect import *
import os
import updateEntryCompletionPercent, deleteEntry, getInputFromUser

def select_entry(index):
    if (index < 1):
        print(f"Could not find an entry at index '{index}'; Please try again.")
        return False # return that the method was unsuccessful

    # display full details of the entry selected
    dbCursor.execute(f"Select id, datetime_posted, entry, progress_percent FROM todo_entries ORDER BY {dbEntryOrderSqlString}  LIMIT 1 OFFSET {index-1}")
    allRecords = dbCursor.fetchall()
    
    if len(allRecords) == 0:
        print(f"Could not find an entry at index '{index}'; Please try again.")
        return False # return that the method was unsuccessful
    print("test")
    print(allRecords[0][0])
    entryId = int(allRecords[0][0])
    print(entryId)

    print(f"{allRecords}")

    # display menu and await response
    print(menu_string_from_file())

    selectProgram = True
    while selectProgram:

        # get formatted input from the user
        optionChosen = getInputFromUser.get_input_from_user()

        selectProgram = False # by default, end the loop

        match optionChosen[0]:
            case "u" | "update":
                updateEntryCompletionPercent.update_entry_completion_percent(entryId, optionChosen[1])
            case "c" | "complete":
                updateEntryCompletionPercent.update_entry_completion_percent(entryId, 100)
            case "i" | "incomplete":
                updateEntryCompletionPercent.update_entry_completion_percent(entryId, 0)
            case "d" | "del" | "delete":
                deleteEntry.delete_entry(entryId)
            case "b" | "back":
                selectProgram = False # do nothing and return to the main script
            case _:
                selectProgram = True # loop again if this option triggers
                # if (option1 == ""):
                print("An invalid option was selected; Please try again.")

    return True # return that the method completed successfully

def menu_string_from_file():
    with open(os.path.dirname(os.path.abspath(__file__)) + '\menuChoices_select.txt') as menuFile:
        menuString = menuFile.read()
    return menuString
