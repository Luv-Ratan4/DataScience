set1 = {2,4,5,4,5,1,2}
print(set)

set2 = {2,4,"Luv", True, 4,5,665,"This is a string", False}
print(set2)
print(type(set2))

setT = {} #This is an empty dictionary not an empty set
emptySet = set() #This is how we initialise an empty set 
print(type(setT), type(emptySet))

for values in set2:
    print(values, end=" ")

#SET METHODS ------------------------------------------------------------

s1 = {1,2,4,6}
s2 = {1,2,5,9,8}

print(s1.union(s2)) #returns Union in sets (Mathematics)
print(s1, s2)
print(s1.intersection(s2)) #returns  only the common items (Mathematics) 
print(s1.symmetric_difference(s2)) #removes intersection and returns the combined items
s1.update(s2) #returns all items of s2 in s1 without dublicating the common items 
print(s1)
print("Is disjoint? ", s1.isdisjoint(s2)) #Returns true if two sets have no elements in common
print("Is Subset? ", s1.issubset(s2)) #Returns true if s1 has all the elements of s2 but s2 has more elements
print("Is Superset? ", s1.issuperset(s2)) #Returns true if s2 has all the elements of s1 but s1 has more elements

#DISCARD and REMOVE, removes throws error when the item is not in the set but discard does not throws an error
s1.discard(1) 
print(s1) #1 will no be there in the set 

#POP - pops out a random item from the set and returns that value
print(s1.pop())

#DELETE AND CLEAR - delete completely removes the set from existence while clear only cleans the set items and makes it an empty set

