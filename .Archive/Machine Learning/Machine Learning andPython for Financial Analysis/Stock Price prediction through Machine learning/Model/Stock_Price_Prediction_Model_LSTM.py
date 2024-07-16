import pandas as pd
import plotly.express as px
from copy import copy
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import Ridge
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

preData = []


def importFiles():
    global preData  # Use global to modify the global variable within the function
    data = []
    if len(preData) == 0:
        preData = pd.read_csv('medicamen_prices.csv')
        data = preData
        return data
    else:
        data = preData
        return data


def interactive_plot(df, title):
    fig = px.line(title=title)
    for i in df.columns[1:]:
        fig.add_scatter(x=df['Date'], y=df[i], name=i)
    fig.show()


def individual_stock(price_df, name):
    return pd.DataFrame({'Date': price_df['Date'], 'Close': price_df[name]})


def trading_window(data):
    # 1 day window
    n = 1
    # Create a column containing the prices for the next 1 days
    data['Target'] = data[['Close']]
    # return the new dataset
    return data


def main():
    stock_prices = importFiles()
    price_volume_df = individual_stock(stock_prices, 'medicamen')
    training_data = price_volume_df.iloc[:, 1:3].values
    scalar = MinMaxScaler(feature_range=(0, 1))
    training_data_scaled = scalar.fit_transform(training_data)

    X = []
    Y = []

    for i in range(1, len(price_volume_df)):
        X.append(training_data_scaled[i - 1:i, 0])
        Y.append(training_data_scaled[i, 0])

    X = np.asarray(X)
    Y = np.asarray(Y)

    split = int(0.8 * len(X))
    X_train = X[:split]
    Y_train = Y[:split]
    X_test = X[split:]
    Y_test = Y[split:]

    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    inputs = keras.layers.Input(shape=(X_train.shape[1], X_train.shape[2]))
    x = keras.layers.LSTM(180, return_sequences=True)(inputs)
    x = keras.layers.Dropout(0.3)(x)
    x = keras.layers.LSTM(180, return_sequences=True)(x)
    x = keras.layers.Dropout(0.3)(x)
    x = keras.layers.LSTM(180)(x)
    outputs = keras.layers.Dense(1, activation='linear')(x)

    model = keras.Model(inputs=inputs, outputs=outputs)
    model.compile(optimizer='adam', loss="mse")
    model.summary()

    # Train the model
    history = model.fit(
        X_train, Y_train,
        epochs=20,
        batch_size=32,
        validation_split=0.2
    )

    # Make prediction
    predicted = model.predict(X)

    # Append the predicted values to the list
    test_predicted = []

    for i in predicted:
        test_predicted.append(i[0])

    df_predicted = price_volume_df[1:][['Date']]

    df_predicted['Predictions'] = test_predicted

    close = []
    for i in training_data_scaled:
        close.append(i[0])

    df_predicted['Close'] = close[1:]

    # Recreate and fit MinMaxScaler to the original data
    scalar = MinMaxScaler(feature_range=(0, 1))

    value = scalar.fit(
        price_volume_df.iloc[:, 1:2])  # Replace your_original_data with the original data used for normalization

    # Extract the normalized columns
    normalized_columns = df_predicted[['Predictions']]
    normalized_columns1 = df_predicted[['Close']]

    # Use inverse_transform to convert normalized data back to the original scale
    original_data = scalar.inverse_transform(normalized_columns)
    original_data1 = scalar.inverse_transform(normalized_columns1)
    # Update the DataFrame with the original data
    df_predicted[['Predictions']] = original_data
    df_predicted[['Close']] = original_data1

    # Display the result
    print(df_predicted)
    return df_predicted


def loopFunction():
    global preData
    # Initialize an empty DataFrame to store the cumulative data
    preData = pd.DataFrame(columns=['Date', 'medicamen'])
    countClose = 1235
    chartData = pd.DataFrame(columns=['Date', 'medicamen'])
    for i in range(99):
        # Assuming main() returns a DataFrame with columns 'Date' and 'Predictions'
        temp = pd.DataFrame(main())
        chartData = temp.copy()
        # Copy data from temp to numpy arrays
        date_array = np.array(temp['Date'])
        predictions_array = np.array(temp['Predictions'])
        # Copy data from arrays to preData DataFrame
        preData.loc[1:, 'Date'] = date_array
        preData.loc[countClose:, 'medicamen'] = predictions_array[countClose - 1]
        print(preData['medicamen'][countClose])
        countClose += 1
    interactive_plot(chartData, "Medicamen")
    chartData.to_csv('Medicamen Biotech Predicted Stock Prices.csv', index=False)


loopFunction()
