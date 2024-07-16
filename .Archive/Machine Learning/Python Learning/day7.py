# Conditional statements (If-Else)

# a = int(input("Enter Your Age "))
# print("Your age is", a)

# if a > 18:
#     print("You can drive")
# else:
#     print("You Cannot drive")
# print("This will be printed because it is not a part of if else due to it's intendation")

# Conditional Operators - >, <, <=, >=, ==, !=
# Intendation - this signifies that the new block of code is started

#  --------------------------------

applePrice = 10
budget = 190

if(budget - applePrice > 0) :
    print("You can buy 1 KG of apples")
elif (budget - applePrice > 190): 
    print("You can buy apples")
else :
    print("You cannot buy apples ")


a = input("Enter your Name")
b = int(input("Enter your Age"))

if(b > 18):
    print("you are old enough to drive")
    if(b>21):
        print("You are old enough to drink")
        if(b>30):
            print("You are old enough to Become a Prime Minster")
        else:
            print("You are not old enough to become a prime minister")
    else:
        print("You are not old enough to drink")
else:
    print("Hey ", a, " Kiddo!")