import pandas as pd
import plotly.express as px
from copy import copy
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

stock_prices = pd.read_csv('Model/wipro_prices.csv')
stock_volume = pd.read_csv('wipro_volume.csv')


def normalize(df):
    x = df.copy()
    for i in x.columns[1:]:
        x[i] = x[i] / x[i][0]
    return x


def interactive_plot(df, title):
    fig = px.line(title=title)
    for i in df.columns[1:]:
        fig.add_scatter(x=df['Date'], y=df[i], name=i)
    fig.show()


# interactive_plot(normalize(stock_prices), 'Normalized Stock Prices')
# interactive_plot(normalize(stock_volume), 'Normalized Stock Volume')


def individual_stock(price_df, vol_df, name):
    return pd.DataFrame({'Date': price_df['Date'], 'Close': price_df[name], 'Volume': vol_df[name]})


def trading_window(data):
    # 1 day window
    n = 1

    # Create a column containing the prices for the next 1 days
    data['Target'] = data[['Close']].shift(-n)

    # return the new dataset
    return data


price_volume_df = individual_stock(stock_prices, stock_volume, 'Wipro')

price_volume_target_df = trading_window(price_volume_df)
price_volume_target_df = price_volume_target_df[:-1]

from sklearn.preprocessing import MinMaxScaler

sc = MinMaxScaler(feature_range=(0, 1))
price_volume_target_scaled_df = sc.fit_transform(price_volume_target_df.drop(columns=['Date']))
X = price_volume_target_scaled_df[:, :2]
Y = price_volume_target_scaled_df[:, 2:]

print(X.shape, Y.shape)

split = int(0.7 * len(X))
X_train = X[:split]
Y_train = Y[:split]
X_test = X[split:]
Y_test = Y[split:]


def show_plot(data, title):
    plt.figure(figsize=(13, 5))
    plt.plot(data, linewidth=3)
    plt.title(title)
    plt.grid()


regression_model = Ridge()
regression_model.fit(X_train, Y_train)
lr_accuracy = regression_model.score(X_test,Y_test)
print(lr_accuracy)


#   Make Prediction
predicted_prices = regression_model.predict(X)
predicted = []
for i in predicted_prices:
    predicted.append(i[0])

close = []
for i in price_volume_target_scaled_df:
    close.append(i[0])
df_predicted = price_volume_target_df[['Date']]
df_predicted['Close'] = close
df_predicted['Predictions'] = predicted

# interactive_plot(df_predicted, 'Original Vs Predictions')

stock_prices = pd.read_csv('Model/medicamen_prices.csv')
stock_volume = pd.read_csv('medicamen_volume.csv')

price_volume_df_medicamen = individual_stock(stock_prices, stock_volume, 'medicamen')

training_data = price_volume_df_medicamen.iloc[:,1:3].values
scalar = MinMaxScaler(feature_range=(0,1))
training_data_scaled = scalar.fit_transform(training_data)

X = []
Y = []

for i in range(1, len(price_volume_df_medicamen)):
    X.append(training_data_scaled[i-1:i, 0])
    Y.append(training_data_scaled[i,0])

X = np.asarray(X)
Y = np.asarray(Y)

split = int(0.7 * len(X))
X_train = X[:split]
Y_train = Y[:split]
X_test = X[split:]
Y_test = Y[split:]

X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))



















