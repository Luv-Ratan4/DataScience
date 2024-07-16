import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from sklearn.externals import joblib

# Load the data set using the pandas dataframe using the read_csv function
df = pd.read_csv("ml_house_data_set.csv")   #PD means pandas

#Now we will do the feature engineering work if required

# Remove the fields from the data set that we don't want to include in our model

del df['house_number']  #using the dictionary delete function
del df['unit_number']
del df['street_name']
del df['zip_code']


# Replace categorical data with one-hot encoded data
features_df = pd.get_dummies(df, columns=['garage_type', 'city'])   #using the pandas inbuilt function

# Remove the sale price from the feature data - OUTPUT DATA

del features_df['sale_price'] #using the dictionary delete function . Here we are deleting the output

# Create the X (Input Features) and y (Output) arrays
X = features_df.as_matrix()         #we want the feature in the form of numpy matrix data type and not in pandas dataframe
y = df['sale_price'].as_matrix()    #This will be our output data