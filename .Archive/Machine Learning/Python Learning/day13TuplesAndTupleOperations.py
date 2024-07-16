tup = (1, 4, 5, 6)
print(tup)
print(type(tup))
tup = (1,) #if there is just one digit then python thinks that it is an integer/string/boolean value. Therefore we have to give a comma if there is just one digit
print(tup) 

newTup = (2,4,2, "Luv", True)
print(newTup)

#Indexing is same in tuples as lists

print(newTup[3])

if "Luv" in newTup:
    print("Yes at index" , newTup.index("Luv"))
tup2 = newTup[1:4]
print(tup2)

#Whenver we try to do some operations in tuple, it returns us a new tuple


#OPERATIONS ON TUPLES --------------------------------------------------------

#we can directly concateante two tuples into a new tuple

tup3 = tup + tup2 + newTup + ("This is a new tuple",)
print(tup3)

print(tup3.count(2)) #Counts all occurrences of 2 in the tuple
print(tup3.index("Luv")) #Index of first occurrence of the tuple
print(tup3.index("Luv", 2, 5)) 
print(len(tup3))
