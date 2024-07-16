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

interactive_plot(df_predicted, 'Original Vs Predictions')



