def get_input_from_user():
    # get user input and format as an array with 2 values
    optionString = input("::").lower()

    optionStringSplit = optionString.split(' ')
    totalOptions = len(optionStringSplit)
    
    option1 = ""
    if (totalOptions > 0):
        option1 = optionStringSplit[0]
    
    option2 = -1
    if (totalOptions > 1 and optionStringSplit[totalOptions - 1].isdigit()):
        option2 = int(optionStringSplit[totalOptions - 1])
    
    return [option1, option2]