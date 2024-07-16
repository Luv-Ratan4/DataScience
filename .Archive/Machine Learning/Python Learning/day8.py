#Match Case

X = int(input("Enter the value of X "))

# X is the variable that we need to match

match X:    #This means check for the value which is inside X if if matches with the cases. Cases are 0, 1, 4 etc here
    case 0:                     #these cases are similar to "If" statement   
        print(X , " is Zero")
    case 1:
        print(X , " is One")
    case 4:
        print(X , " is Four")
    case _:                     #Underscore is used for default case. default case is similar to "else", rest of the cases are "if"
        print(X, " is it's default value")