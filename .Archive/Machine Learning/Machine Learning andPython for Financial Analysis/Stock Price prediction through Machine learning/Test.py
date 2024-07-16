import pandas as pd
import numpy as np

# Sample DataFrame
temp = pd.DataFrame({
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
    'Predictions': [10.5, 11.2, 12.0]
})

# Initialize empty arrays
dateData = np.array([])
medicamenData = np.array([])

# Extract and assign values to arrays
dateData = temp[['Date']].values
medicamenData = temp[['Predictions']].values

# Display the NumPy arrays
print("Date array:")
print(dateData)

print("\nMedicamen array:")
print(medicamenData)
