# # To open a file
# f = open('fruits_input.txt', 'r')  # (fileName, mode such as reading, writing etc.)
#
# # To Read a file
# text = f.read()  #Reading the contents of the file and saving it to a variable
# print(text)
# f.close()
#
# # NOTE - We can't read the file in the write mode and vice versa.
# # r - This is the default mode of the file
# # In the write mode, if we open a file that does not exist yet then it will be created
# # a - when we want to keep the existing content of the file intact and add new content
# # x - creates a file
#
# # To Write on a new file
# f = open('fruits_input2.txt', "w")
# f.write("Hello World")
# f.close()
#
# # To append on an existing file
# f = open('fruits_input2.txt', 'a')
# f.write(' Repeat')
# f.close()
#
#
# # Using the WITH keyword - we don't need to close the file here
# with open('fruits_input2.txt', 'a') as f:
#     f.write(" New Things")

# ----------------------------------------------------------------------


with open('fruits_input.txt', 'r') as f:
    while True:
        line = f.readline()
        myList = line.split()
        print(myList)
        for item in myList:
            print(item)
        if not line:
            break
    print(type(line))

f = open('sample_text_file.txt')
newContent = f.read()
content = f.readline()
old = f.readlines()

print(content, type(content), newContent, old)
f.close()

















