


#PRINT STATEMENT ------------------------------------------


print("Hello world"),
print("This is our first python program"), 
#"print" keyword prints anything that is inside the function
#this file is actually a script



#ESCASPE SEQUENCE CHARACTERS ---------------------------------------------


print("This is first line \nThis will be in new line"), #we can also write a comment here 

print("This is a code \"unfortunately\""),



# We can add multiple type of things in the same line such as
print("This is first statement", 45, "This \n should \n be \n next \n line", 45, sep="+"), 
print("A string", 451, 45) 

# we can combine them with the keyword "sep" as follows
print("First string", 12, 2, sep="+", )

# we can use anything inside sep example
print("Second string", 12, 2, sep="/", )

# if we want to print anything at the end of any line statement, then we use the "end" keyword
print("Third string", 12, 2, end="009" )
print("Forth string", 12, 2, sep="45", end=" 009\n" )

#VARIABLES -----------------------------------------------------

a = 1451851
print(a)

b = "Luv Ratan"
print(b)

c = True
print(c)
b = True #We are creating a new data type in b
print(b)

d = None
print(d)

e ="String again"
print(e)
print("The type of ", a , "is " , type(a) )
print("The type of ", b , "is " , type(b) )
print("The type of ", c , "is " , type(c) )
print("The type of ", d , "is " , type(d) )
print("The type of ", e , "is " , type(e) )

# DATA TYPES ----------------------------------------------------

#There are 5 inbuilt data types in Python

'''

- Strings
- Boolean
- Numbers
- Sequence
- mapped data/dictionary 

'''