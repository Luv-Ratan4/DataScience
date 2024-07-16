"""

print('He said, "I want to eat an Apple."')

print(""This is a multi-line String.
      For Example this is a new line.
      And this is a new line again"")

ourString = "This is a string"

print(ourString[0]) #This will print T
print(ourString[4]) #This will print a space
print(ourString[2]) #This will print i
print(ourString[17]) #This will give an index error

#To print all the characters of the string without any hassle, we can use for loop

for characters in ourString:
    print(characters)

"""
#STRING METHODS --------------------------------------------------------------------------------

# Strings are immutable

a = "luvRatan"
print(len(a))
print(a.upper())
print(a.lower())

b = "!!!!Hello!l!!!!!!!!!!!!!!!!!"

#This removes Trailing characters
print(b.rstrip("!")) 

#Changes ALL occurrences to the new given characters
print(b.replace("Hello", "Hello World"))

#Split returns a new array- Whenever split finds the character given inside the brackets, it will add an element inside the array separated by a commma. This new element will be all the elements after the bracket element till it finds a new bracket element or the string ends 
print(b.split("H"))

#This will only capitalise the first line of the paragraph not the recurring lines after the full stop. The other words are converted to lower case(if any upper case is there)
a = "this is first line. This is second lIne."
print(a.capitalize())


#Center method aligns the string, To make it that many characters long as many we specify in the syntax
print(a.center(41))
print(len(a))
print(len(a.center(5)))

#Count method as the name suggests, counts the occurence of the specified letters or numbers in the string
d = "Hey my name is Luv and Luv is not spelled as Love 9"
print(d.count("Luv")) #This will give 2

#ends with check if the string ends with this given text or not
print(d.endswith("luv")) #false
print(d.endswith("Love")) #true
print(d.endswith("name", 5, 11)) #this means, whatever the text is in between 5 and 11, does it ends with name?
print(d.find("my")) #This will return 4 because 4 my is in 4th position, it only detects the first occurence
print(d.find("jik")) #This will return -1
#print(d.index("hek")) #This will return an error, it is similar to find but it gives error when the item is not found. Used for error handling
print(d.isalnum()) #returns true if the string has alphabet or numerical values and if anything else, it will return false. Also the string should not have spaces
print(d.isalpha()) #returns true if the number only has alphabets else returns false
print(d.islower()) #returns true if all the alphabets are in lower case
print(d.isprintable()) #returns true if all the alphabets are printable. Example of Non Printable items - '\n', \'t', '\r', '\x16', '\xlf'
print(d.isspace()) #returns true if we have whitespaces in the code. Whitespace are made using spacebar or tab
e = "Is Title Or Not"
print(e.istitle()) #returns true if the first alphabet of each word in the string are in capital letters
print(e.isupper()) #returns true if all the letters of the string are in upper case
print(e.startswith("Is")) #returns true if the given string starts with the given characters inside the round brackets
print(e.swapcase()) #converts all the lower case items to upper case and all the upper case items to lower case
print(d.title()) #converts the letter into tilte
 