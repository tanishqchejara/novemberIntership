import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score
import requests
from io import StringIO

# Load data from Google Sheets URL
path = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRTK2NvcndgPX41Czu6Ft2Ho_nE-z50BgTqdzwFW0rsJ2nvyNLe2DoIg1COzUbgw80oaRBjfy5-WtFk/pub?output=csv'
response = requests.get(path)
data = response.content.decode('utf-8')

# Read the data using pandas, handling the error in a different way
try:
    df = pd.read_csv(StringIO(data))
except pd.errors.ParserError as e:
    print("ParserError:", e)
    print("Attempting to skip bad lines...")
    df = pd.read_csv(StringIO(data), error_bad_lines=False)

print('\nReading the Data:')
print(df.head())

# Check the column names to verify
print('\nColumn Names:')
print(df.columns)

# Check for missing values in 'Y' column
print("\nNumber of missing values in 'Y' column:", df['y'].isnull().sum())

# Drop rows with missing values in 'Y' column
df.dropna(subset=['y'], inplace=True)
# Selecting columns 'X' and 'Y' for modeling
x = df['x'].values.reshape(-1, 1)  # Reshape to a 2D array if 'X' is a single feature
y = df['y'].values

# Creating a scatter plot of the data
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot of X vs Y')
plt.show()

# Splitting the data into training and testing sets
msk = np.random.rand(len(df)) < 0.8
train_x = x[msk]
train_y = y[msk]
test_x = x[~msk]
test_y = y[~msk]

# Modeling
reg = linear_model.LinearRegression()
reg.fit(train_x, train_y)

print('\nModel Coefficients:')
print('Coefficient:', reg.coef_[0])
print('Intercept:', reg.intercept_)

# Predictions on the test set
predictions = reg.predict(test_x)

# Model Evaluation
print('\nModel Evaluation:')
print('R2-Score:', r2_score(test_y, predictions))

# Plotting the regression line on the scatter plot
plt.scatter(x, y)
plt.plot(test_x, predictions, color='red', linewidth=3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Fit')
plt.show()
