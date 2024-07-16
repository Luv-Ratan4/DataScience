#Loops
'''
name = "My complete name is Luv Ratan"

# here "i" is a variable that will iterate trough each element of the name string and value of i will keep on changing according to the value inside the name object
for i in name:  
    print(i, end=" ")
print("")

names = ["Luv", "Lalita", "Ratna" , "Nehal", "Nana", "Nani"]

for i in names:
    print(i, end=" ")
    for j in i:
        print(j, end=" ")

#range in loops -------------------------------------

for k in range(5):   #it will not include 5 because range it "n-1"
    print(k)
for k in range(5, 50):  #it will start from 5 but not include 50 because range it "n-1"
    print(k, end=" ")

#step--------------------------

for k in range (1, 50, 2): #it will jump 2 steps 
    print(k)

'''


#WHILE LOOPS

i = int(input("Enter a number "))
while(i<3):         #This condition will be checked in every iteration
    print(i)
    i = i+1


j = int(input("Enter a number"))

while (j>0):
    print(j , end=" ")
    j = j-1
else:
    print("Number not in range")