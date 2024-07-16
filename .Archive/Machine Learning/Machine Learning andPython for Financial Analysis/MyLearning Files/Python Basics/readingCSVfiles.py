import csv

with open('sample_csv_file.csv') as f:
    readCSV = csv.reader(f, delimiter=',')  # readCSV is ab object of the class csv.reader, readCSV is also an iterator
    data = list(readCSV)  # The contents of the readCSV object/iterator is converted into a list which is an iterable
    # print(data)  #Prints the complete data

# print(data[1])  #Prints data of first row

#  Combine the first and last name of the person
fullName = []
dollarValues = []
for row in data:
    if row[0] == 'first':
        continue
    fullName.append(row[0] + " " + row[1])
    dollarValues.append((row[5]))
print(fullName)
print(dollarValues)


#Mini Challenge -------------------------

with open('S_P500_Stock_Data.csv', 'r') as P:
        data = list(csv.reader(P, delimiter=','))


prices = []
count = 0
for rows in data:
    prices.append(rows)
    count +=1
    if count == 6:
        break
print(prices)
