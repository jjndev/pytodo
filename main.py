import os
import addEntry, selectEntry, listEntries, updateEntryCompletionPercent, getInputFromUser

# function to read the respective menu files 
def menu_string_from_file():
    with open(os.path.dirname(os.path.abspath(__file__)) + '\menuChoices_main.txt') as menuFile:
        menuString = menuFile.read()
    return menuString



# create a boolean variable 
mainProgram = True
printList = True

print("ToDo List Application\n=====================\n")

while mainProgram: # while True
    #initialise the songs_menu function with mainMenu variable
    
    if printList:
        listEntries.list_entries()
        print(menu_string_from_file())
        printList = False

    # get formatted input from the user
    optionChosen = getInputFromUser.get_input_from_user()

    match optionChosen[0]:
        case "n" | "new":
            addEntry.add_entry()
            printList = True
        case "s" | "select":
            printList = selectEntry.select_entry(optionChosen[1])
        case "c" | "complete":
            updateEntryCompletionPercent.update_entry_completion_percent(optionChosen[1], 100)
            printList = True
        case "e" | "exit" | "quit":
            mainProgram = False # end the loop
        case _:
            # if (option1 == ""):
            print("An invalid option was selected; Please try again. (Type 'e' to exit the application.)")

      
input("Press Enter to exit the application.")
    
