import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""

# Creating a Line Chart

stocks_data = pd.read_csv('stocks.csv')  # Reading CSV data
stocks_data.plot(x='Date', y='AAPL', label="Apple stock prices",
                 linewidth=3, color='r')  # Creating a line Chart
plt.ylabel("Price")  # Labelling the Y axis as "Price"
plt.legend(loc='upper right')  # Moving title to upper right
plt.title('My First Line Chart')  # Giving title to the chart


# Creating a scattered chart

daily_returns = pd.read_csv('daily_returns.csv')
X = daily_returns['GOOG']
Y = daily_returns['sp500']
plt.scatter(X, Y)
plt.xlabel('Google Daily Returns')
plt.ylabel('SnP 500 Daily returns')   #Create a Scattered chart


# Creating a pie Chart

values = [20,45,55,2,5,17]  #Values which will contribute to the total pie chart
colors = ['g','r','b','y','m','c']  #Colors of the allocation
labels = ['AAPL', 'GOOG', 'ATNT', 'TESLA', 'AMAZON', 'WIPRO']   #Labels of the different pieces
explode = [0,0.2,0,0,0,0.3] #Using this the particular defined piece will look 
#like it is coming out of the pie chart but is optional
plt.figure(figsize=(10,10)) #Defines the size of the chart but it optional
plt.pie(values, colors=colors,labels=labels, explode=explode)   #Making a pie chart using Matplotlb
plt.title('Stocks Portfolio')   #Giving title to the Chart


#Creating a Histogram

daily_returns = pd.read_csv('daily_returns.csv')
mu = daily_returns['AAPL'].mean()       #statictics Concept used for title
sigma = daily_returns['AAPL'].std()     #statictics concept used for title
plt.figure(figsize=(7,5))               
num_bins = 100  #Number of divisions of the data, for example in which proportion 
#data will be divided into different bars
plt.hist(daily_returns['AAPL'], num_bins)   #Making a Histogram using Matplotlib
plt.grid()  #Adding a grid to the chart
plt.title('Histograms: {} {}'.format(mu, sigma))    #Adding a title to the histogram
#plt.hist(daily_returns['GOOG'], 30)



#Creating multiple plots in the same Chart

stocks_data = pd.read_csv('stocks.csv')  # Reading CSV data
stocks_data.plot(x='Date',y =['AAPL', 'sp500'], linewidth= 3)
plt.ylabel("Price")
plt.title("Stock Prices")
plt.grid()

stocks_data.plot(x='Date', y=['AAPL', 'GOOG', 'sp500'])
plt.legend( loc='upper center')
plt.grid()


#Creating a Sub-Plot

stocks_data = pd.read_csv('stocks.csv')  # Reading CSV data

plt.figure(figsize=(10,5))

plt.subplot(2,1,1)  #1 row 2 columns and this one is the 1st column
plt.plot(stocks_data['AAPL'], 'r--')    #SubPlot with red color line and breaked line
plt.grid()

plt.subplot(2,1,2)  #1 row 2 columns and this one is the 2nd column
plt.plot(stocks_data['sp500'], 'b')     #SubPlot with blue color line 
plt.grid()

#Creating 3D plots - Using Matplotlib 3D plotting

from mpl_toolkits.mplot3d import Axes3D
daily_returns = pd.read_csv('daily_returns.csv')
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection = '3d')    #Defining a 3D subplot

x = daily_returns['AAPL'].tolist()  #Defining X axis
y = daily_returns['sp500'].tolist() #Defining Y axis
z = daily_returns['GOOG'].tolist()  #Defining Z axis
ax.scatter(x,y,z, c = 'r', marker = 'o')    #Creating the plot
ax.set_xlabel('X Label')    #Set Labelling
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

#Creating Box Plot

np.random.seed(20)

data1 = np.random.normal(200,20,2000)
data2 = np.random.normal(60,30,2000)
data3 = np.random.normal(70,20,2000)
data4 = np.random.normal(40,5,2000)
data= [data1,data2,data3,data4]

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
bp = ax.boxplot(data)

"""




































