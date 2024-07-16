import numpy as np

"""
my_list = [10,20,51,54,51,52,52,15,78456,9,65,25,156,16,43,4,6]

#  creating a numpy array from  a list
x = np.array(my_list)
print(x, type(x))
matrix = np.array([[5,15,12,51,541,5,12],[7,541,31,6,454,21,85]])
print(matrix, type(matrix))

challenge = [[4,6,8,7],[20,6,5,9]]
print(challenge, type(challenge))
challengeMatrix = np.array(challenge)

print(challengeMatrix, type(challengeMatrix))



#  NumPy built-in methods and functions

#  rand() - create the given amount of random float numbers between 0 and 1 uniformly distributed

print("List of uniformly distributed", np.random.rand(5))
print("Matrix of uniformly distributed", np.random.rand(5,5))  # Creates a 5 * 5 matrix of random float numbers
# between 0 and 1.
print("List of normally distributed", np.random.randn(5))  # Creates list of 5 random float numbers between 0 and 1
# normally distributed.
print("Gives one random integer between the two given numbers", np.random.randint(5, 10))
print("Gives a list of random integers between the two given numbers", np.random.randint(5, 10, 10))
print("Evenly spaced values within a given interval (ARRAY and RANGE)", np.arange(1,54))
print("Evenly spaced values within a given interval (ARRAY and RANGE) with 5 steps", np.arange(1,54,5))
print("Creates a numpy matrix of 0 and 1 of the given size ",np.eye(15))
print("Creates a numpy array of only ones of the given size", np.ones(10))
print("Creates a numpy matrix of only ones of the given size", np.ones((15,15)))
print("Creates a numpy matrix of only zeros of the given size", np.zeros((15,15)))

print(np.random.randint(int(input("Enter your first number: ")),int(input("Enter your second number: ")), 20))

"""

"""
myList = [-30,4,50,60,25,151,47,585]
array = np.array(myList)
print(type(array), array)

print(len(array))  #Length of numpy array
print(array.shape)  #Order of the matrix - (4,5) or (9,0) etc
print(array.dtype)  #type of data in the numpy array

# RESHAPE 1D array into a matrix

matrix = array.reshape(2,4)  #Reshape the numpy array of size 8 into a matrix with 2 rows and 4 columns
print(matrix)

print(matrix.max(), matrix.min())  #Return the maximum and minimum values of the matrix or array
print(matrix.argmax())  #Index of the maximum value
print(matrix.argmin())  #Index of the minimum value


# Mini Challenge 3
print((np.arange(300,500,10)).reshape(4,5))

# Mini Challenge 4
challenge4 = np.random.randint(-1000,1000,400).reshape(20,20)
print(challenge4, challenge4.max(), challenge4.min(), challenge4.mean(), challenge4.shape)


--------------------------------------------------------------------------------------------------------------------
"""

# Mathematical operations in numpy
"""

x = np.arange(1,10)
y = np.arange(1,10)
print(x+y)  # Sum individual values of x with respective values of y
print(x**2)  # Square every value of x
print(np.sqrt(x))  #Square root of every value of array x
print(np.exp(y))    #Exponential values

--------------------------------------------------------------------------------------------------------------------
"""

"""
print(np.array(["Luv",115 ,51515,1515]))
x = np.array([20,40,50,21,15, 151,515,1581,12684,31])
print(x[5])  #Numpy Array have same indexing as python lists because they are essentially same
# Matrix in numpy is essentially list of lists in python
print(x[1:5])  #Return the elements from index 1 to index 5
x[0:5] = 15     #Change the elements of matrix from index 0 to index 5 and set them to 50, BROADCASTING
print(x)


matrix = np.random.randint(1,10,(5,5))

print(matrix)

row = int(input("Enter your row number: "))
col = int(input("Enter your col number: "))
print("The content of row number {row} is {matrix[row]}")  #Prints content of the row

print(f"The content of row = {row} and column = {col}  is {matrix[row][col]}")  #Print item at given row and column

print(matrix)
print(matrix[:3])   #Gives a sub-matrix of the parent matrix till row 3
# : means all the columns, :3 means all the columns but only 3 rows
print(matrix[:,2:])  #Means all the rows but only start with 2nd column
print(matrix[2:,2:])   #come to second row, then come to second column and everything from there

# Challenge 6
x = [[2,30,20,-2,-4],[3,4,40,-3,-2],[-3,4,-6,90,10],[25,45,34,22,12],[13,24,22,32,37]]
matrix = np.array(x)
matrix[4] = -1  #Broadcasting
print(matrix)
matrix[:2,2:] = matrix[:2,2:] * 2
print(matrix)

--------------------------------------------------------------------------------------------------

# Elements Selection (Conditional)

matrix = np.random.randint(1, 10, (5, 5))
print(matrix)

newMatrix = matrix[matrix > 3]  # Gives elements of the matrix that are greater than 3
print(newMatrix)
newMatrix = matrix[matrix % 2 == 0]  # Gives elements of the matrix that are divisible by 2
print(newMatrix)

# Mini Challenge

X = np.array([[2, 30, 20, -2, -4],
              [3, 4, 40, -3, -2],
              [-3, 4, -6, 90, 10],
              [25, 45, 34, 22, 12],
              [13, 24, 22, 32, 37]])

X[X % 2 == 1] = 25  #BROADCASTING
X[X < 0] = 0
print(X)

"""

















