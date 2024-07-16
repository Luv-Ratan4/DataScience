'''
dic = {
    "key1" :"Element 1",
    "key2" : 2525,
    "key3" : ["45",15,"Luv"]
}

print(dic)

for keys in dic:
    print(dic[keys])        #method 1 to access values inside dictionary
    print(dic.get(keys))    #method 2 to access values inside dictionary

print(dic.keys())   #This will return an array of keys

for keys in dic:
    print(keys)     #This will give all the keys
    print(f"The value for {keys} is {dic[keys]}")

for keys, values in dic.items(): #This is destructuring of keys and values from dictionary
    print(f"{keys} : {values}")
'''


#Dictionary Methods-------------------------------------------------

ep = {122: 45, 129: 58, 55: 99, 670: 69}
ep2 = {22:55, 57:889, "item": "test"}

ep.update(ep2)
ep2.clear()
print(ep)
print(ep2)
empt = {} #This will return an empty dictionary
ep.pop(122) #This will remove the specified item from the dictionary with the given key
ep.popitem()    #This will remove the last item from the dictionary
del ep[55] #This will remove the speicified item from the dictionary
print(ep)
del ep #completely deletes the dictionary