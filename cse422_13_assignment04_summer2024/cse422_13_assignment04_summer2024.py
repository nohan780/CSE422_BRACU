# -*- coding: utf-8 -*-
"""24141092_Nohan Ahmed_CSE422_13_Assignment04_Summer2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CV3VPL1N2QidcnXoMeGcKvWyusW0HgbQ
"""

import pandas as pd
import numpy as np

#data load
volunteer = pd.read_csv("/content/Housing Price Prediction Data.csv")
volunteer.shape

#checking where are the missing values are...
volunteer.isnull().sum()

#handling missing values by using mode...

handle = volunteer['Bedrooms'].mode()[0]
volunteer['Bedrooms'].fillna(handle, inplace=True)
print(volunteer.isnull().sum())

#handling the categorical values by one-hot encoding.... dropping the first one, because if the other two are false then obviously the other one will be true, and as well as it will handle the multicolinearity problem in linear regression model..

volunteer = pd.get_dummies(volunteer, columns= ['Neighborhood'], drop_first=True)
print(volunteer.head())

#assign true and false as 0 and 1
volunteer = volunteer.astype(int)
print(volunteer.head())

#feature selection... I assume that if the corelation value is over +-0.75 the I will delete that column... as there is no such column we find here so no need to delete any...
corr_matrix = volunteer.corr()
print(corr_matrix)

#checking the standart deviation for feature scaling.... as we can see that the std is very high for price column... so we have to use robust scaler...
print(volunteer.std())

#split the train set and using the robust scaler
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split

X = volunteer.drop('Price', axis=1)
y = volunteer['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=10)

robust_scaler = RobustScaler()
X_train_scaled = robust_scaler.fit_transform(X_train)
X_test_scaled = robust_scaler.transform(X_test)

volunteer.head()