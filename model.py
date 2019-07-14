#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 20:25:35 2019

@author: hp
"""

# Data Preprocessing

# Importing the libraries
import pandas as pd
import pickle


# Importing the dataset
dataset = pd.read_csv('httpftp.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 5].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder

# Encoding the Independent Variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)     

 
# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""



# Random Forest 
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=10)
model.fit(X_train, y_train)

# Predicting the Test set results
y_pred = model.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# save the model to disk
"""filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

joblib.dump(model, 'model.pkl')"""
filename = 'finalized_model.sav'
saved_model = pickle.dump(model, open(filename, 'wb'))

