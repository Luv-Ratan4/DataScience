

#Functions - When we want to reuse a block of code again and again with different input and output values, we create a function

'''

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))



def calculateGmean(a, b):

    gmean = (a*b)/(a+b)
    print(gmean) 
    if(a>b):
        print(a , " is greater than " , b)
    elif(a<b):
        print(b ,   " is greater than " , a)
    else:
        print("Both are equal")


calculateGmean(a,b)

def islesser (a, b):
    pass                #pass means you can ignore this function and I will complete it later

'''

#Functions with arguments-----------------------------------------------------
#Types of arguments - Default, Keyword, Variable, Required

#Default arguments

def average(a=9,b=10):              
    print("The average is ", (a+b)/2)

average() #If we don't pass any arguments explicitly here while calling the function, it will take in default arguments.
average(4) #a = 4, b = 10
average(b=14) # a= 9 and b =14

#keyword arguments
average(b=9, a=20)  #Here we can change the order of the arguments

#Required arguments
def average(a,b=10):              
    print("The average is ", (a+b)/2)

average(20) #Here we can see that we have to provide at lease one argument because the value of a if not denfined in default

#Variable length Argument - This takes in a tuple as an argument
def average(*numbers):
    print("The type of numbers is ", type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The average is: ", sum/len(numbers))
    return(numbers) #This returns the complete tuple and comes out of the function

print(average(1,2.3,4,5.5,6))