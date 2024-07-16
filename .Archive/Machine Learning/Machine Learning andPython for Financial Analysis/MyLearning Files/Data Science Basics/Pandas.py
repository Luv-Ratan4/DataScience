import pandas as pd

"""
myList = ['AAPL', 'AMZN', 'T']
label = ['stock#1', 'stock#2', 'stock#3']

x_series = pd.Series(data = myList, index=label)
print(x_series)
print(type(x_series))
print("--------------------------------------------------------------------------------")
print()

# USING DATAFRAME DATA STRUCTURE
bankClientDf = pd.DataFrame({
    'Bank client ID':[111,222,333,444],
    'Bank client name': ['Chanel', 'Steve', 'Mitch', 'Ryan'],
    'Net Worth': [3500,29000,10000,2000],
    'Years with Bank': [3, 4, 9,5]
})   #We can define a pandas dataframe from a dictionary

print(bankClientDf)
print(type(bankClientDf))
print(bankClientDf.head())  #Returns first couple of rows of the dataset
print(bankClientDf.head(2))     #Returns first two rows of the dataset including column header
print(bankClientDf.tail())      #Returns last couple of rows of the dataset
print(bankClientDf.tail(2))     #returns last two rows of the dataset including column header
print("--------------------------------------------------------------------------------")


portfolioData = pd.DataFrame({
    'Stock ticker symbol': ['Wipro', 'TCS', 'Tata Power'],
    'Number of Shares': [200, 100, 151],
    'Price per Share': [150, 20, 522]
})
print(portfolioData)

# Method 1 - Python List method
print(
    portfolioData.values[0][1] * portfolioData.values[0][2] + portfolioData.values[1][1] * portfolioData.values[1][2] +
    portfolioData.values[2][1] * portfolioData.values[2][2])

# Method 2 - Pandas Method
portfolio_value = portfolioData['Number of Shares'] * portfolioData['Price per Share']
# Items of column - Number of shares multiplied by items of column Price per share
print(f'Total portfolio value = {portfolio_value.sum()}')

bank_Data = pd.read_csv('bank_client_information.csv')  # Panda CSV reader
print(bank_Data)
bank_Data.to_csv('Pandas CSV File.csv', index=False)
"""
"""The above statement creates a CSV file with the given data, Index false means that we don't want to include 0,1,
2 etc. index in the file."""
"""
bank_Data.to_csv('Pandas CSV File True.csv', index=True)

housePrices_data = pd.read_html('https://www.ssa.gov/oact/progdata/nra.html')  # Reads the data from the html
# website and stores in the table
print(housePrices_data)



print("--------------------------------------------------------------------------------")


bankClientDf = pd.DataFrame({
    'Bank client ID':[111,222,333,444],
    'Bank client name': ['Chanel', 'Steve', 'Mitch', 'Ryan'],
    'Net Worth': [3500,29000,10000,2000],
    'Years with Bank': [3, 4, 9,5]
})   #We can define a pandas dataframe from a dictionary
print(bankClientDf)

data_loyalCustomers = bankClientDf[(bankClientDf['Years with Bank'] >=5)]   # Return the rows in which the value of
# Years with Bank column is greater than 5
print(data_loyalCustomers)

del bankClientDf['Bank client ID']  #Deletes the bank client ID column
print(bankClientDf)

# Mini Challenge 3

HNIndividuals = bankClientDf[(bankClientDf['Net Worth'] >= 5000)]
print(HNIndividuals)
print((HNIndividuals['Net Worth']).sum())



print("--------------------------------------------------------------------------------")

bankClientDf = pd.DataFrame({
    'Bank client ID': [111, 222, 333, 444],
    'Bank client name': ['Chanel', 'Steve', 'Mitch', 'Ryan'],
    'Net Worth': [3500, 29000, 10000, 2000],
    'Years with Bank': [3, 4, 9, 5]
})


def networth_update(balance):  # Function to update the values of the given column
    return balance * 1.1


bankClientDf['Net Worth'] = bankClientDf['Net Worth'].apply(networth_update)  # Updating the values of the given
# column and assigning the values back to the origin table
print(bankClientDf)

print(bankClientDf['Bank client name'].apply(len))  # Applying inbuilt function length to the elements of the
# column 'Bank client name'

print(bankClientDf['Years with Bank'].sum())  # Applying a function to all the item of the columns collectively


#   Mini Challenge 4

def doubleStockPrice(price):
    return price * 2 +100


bankClientDf['Net Worth'] = bankClientDf['Net Worth'].apply(doubleStockPrice)
print(bankClientDf)
print(bankClientDf['Net Worth'].sum())

print("--------------------------------------------------------------------------------")

bankClientDf = pd.DataFrame({
    'Bank client ID': [111, 222, 333, 444],
    'Bank client name': ['Chanel', 'Steve', 'Mitch', 'Ryan'],
    'Net Worth': [3500, 29000, 10000, 2000],
    'Years with Bank': [3, 4, 9, 5]
})

bankClientDf = bankClientDf.sort_values(by=['Years with Bank'])  # Sorting with the help of the items in the column
# 'Years with bank'

# Alternatively we can directly make changes in the table by adding inplace=true as given below
bankClientDf.sort_values(by=['Years with Bank'], inplace=True)
print(bankClientDf)

# Mini Challenge 5

bankClientDf.sort_values(by=['Net Worth'], inplace=True)
print(bankClientDf)



"""

print("--------------------------------------------------------------------------------")

df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)
df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)
df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)

result = pd.concat([df1, df2, df3])     #Concatenate the data frames together
# print(result)

raw_Data = {
    'Bank Client ID':[1,2,3,4,5],
    'First Name': ['Luv', 'Lalita', 'Nehal','Ratna', 'Divya'],
    'Last Name': ['Ratan', 'Devi', 'Sharan', 'Rawat', 'Ratan']
}
print(raw_Data)
NewBankData = pd.DataFrame(raw_Data, columns=['Bank Client ID', 'First Name', 'Last Name'])

raw_Data2 = {
    'Bank Client ID':[6,7,8,9,10],
    'First Name': ['Ratan', 'Devi', 'Sharan', 'Rawat', 'Ratan'],
    'Last Name': ['Luv', 'Lalita', 'Nehal','Ratna', 'Divya']
}
SecondBankData = pd.DataFrame(raw_Data2)

newData = {
    'Bank Client ID': [1,2,3,4,5,6,7,8,9,10],
    'Annual Salary': [22000,15151,55555,47411,15132,11212,454515,1212,185,418966]
}

AdditionalNewData = pd.DataFrame(newData, columns=['Bank Client ID', 'Annual Salary'])
print(AdditionalNewData)


CompleteData = pd.concat([NewBankData,SecondBankData])  #ADD more rows with same columns
print(CompleteData)

Data = pd.merge(AdditionalNewData, CompleteData, on='Bank Client ID')   #Add more columns with same rows
print(Data)

# Mini Challenge
challengeData = pd.DataFrame({
    'Bank Client ID' : [11],
    'Annual Salary': [99999999],
    'First Name': ['Luv'],
    'Last Name': ['Ratan']
})

Challenge = pd.concat([Data,challengeData], axis=0)
print(Challenge)

























































