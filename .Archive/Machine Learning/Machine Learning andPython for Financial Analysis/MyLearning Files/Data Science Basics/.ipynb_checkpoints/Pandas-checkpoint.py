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
    'Stock ticker symbol':['Wipro', 'TCS', 'Tata Power'],
    'Number of Shares': [200,100,151],
    'Price per Share': [150,20,522]
})
print(portfolioData)

# Method 1 - Python List method
print(portfolioData.values[0][1]*portfolioData.values[0][2]+portfolioData.values[1][1]*portfolioData.values[1][2]+portfolioData.values[2][1]*portfolioData.values[2][2])

# Method 2 - Pandas Method
portfolio_value = portfolioData['Number of Shares'] * portfolioData['Price per Share']     
#Items of column - Number of shares multiplied by items of column Price per share
print(f'Total portfolio value = {portfolio_value.sum()}')

"""

bank_Data = pd.read_csv('bank_client_information.csv')  #Panda CSV reader
print(bank_Data)
bank_Data.to_csv('Pandas CSV File.csv', index=False)
""" The above statement creates a CSV file with the given data, Index false means that we don't want to include 0,1,
2 etc. index in the file."""


bank_Data.to_csv('Pandas CSV File True.csv', index=True)

housePrices_data = pd.read_html('https://www.ssa.gov/oact/progdata/nra.html')       # Reads the data from the html
# website and stores in the table
print(housePrices_data)
































