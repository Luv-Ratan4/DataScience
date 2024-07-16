'''
# Lists are exactly like arrays

l = [3, 5, 6, "Luv", True]
print(l)
print(type(l))
for i in l:
    print(i, end=" ")

i = 0
while i < len(l):
    print(l[i], end=" ")
    i = i + 1

print(l[-3])  # Negative index - This will print 6
print(l[len(l) - 3])  # Positive index - This will result to index 2
print(l[5 - 3])  # Positive index - This will result to index 2
print(l[2])

if "Luv" in l:
    print("Yes")
if 22 in l:
    print("Yes")
else:
    print("Wrong Number")

if "luv" in "luvratan":
    print(True)

print(l)
print(l[:])
print(l[1:])
print(l[2:5])
print(l[1:5:2])

lst = [i for i in range(4)]
print(lst)
lst = [i * i for i in range(10) if i % 2 == 0]
print(lst)

'''

#LIST methods

l = [1,10,55,41,12,3,4,5]
l.append(7) #add 7 at the end of the list
print(l)
l.sort() #sort from smaller to larger
print(l)
l.sort(reverse=True) #sort from larger to smaller
print(l)
l.reverse() #completely reverse to right to left from left to right
print(l)
print(l.index(7)) #print index of the first occurence of 7 if it is in the list
print(l.count(1)) #count number of occurrences of 1 in the list

m = l       #Pass by reference  not by value
m[0] = 0
print(m)
print(l)
n = m.copy() #only copy the items and don't pass the reference or address
n[0] = 1
print(n)
print(m)
l.insert(1, 899) #insert 899 at the 1st index of the list
print(l)
n.extend(l) #add contents of the list l at the end of the list n
print(n)

k = l + m #add contents of list l and m and save it to list k
print(k)