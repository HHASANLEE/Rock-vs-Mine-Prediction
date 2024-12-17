# -*- coding: utf-8 -*-
"""Rock vs Mine prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cPDm_GNEvtr0iQ872rjhFxJl5EWj7A8O
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Processing"""

#loading dataset to a pandas DataFrame
sonar_data = pd.read_csv('/content/sonar[1].csv', header=None)

sonar_data.head()

#number of rows and columns
sonar_data.shape

#describe --> statistical measures of the data
sonar_data.describe()

sonar_data[60].value_counts()

"""M = Mine
R = Rock
"""

sonar_data.groupby(60).mean()

#separating data and labels
X = sonar_data.drop(columns=60,axis=1)
Y = sonar_data[60]

"""Training and Test data"""

print(X)
print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.1, stratify=Y, random_state=1)

print(X_train)
print(Y_train)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training -> Logistic Regression"""

model = LogisticRegression()

#training the logistic regression model with training data
model.fit(X_train, Y_train)

"""Model Evaluation"""

#accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('accuracy on training data: ', training_data_accuracy)

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('accuracy on test data: ', test_data_accuracy)

"""Making a Predictive System"""

#changing the input_data to a numpy array

input_data = (0.0262,	0.0582,	0.1099,	0.1083,	0.0974,	0.2280,	0.2431,	0.3771,	0.5598,	0.6194,	0.6333,	0.7060,	0.5544,	0.5320,	0.6479,	0.6931,	0.6759,	0.7551,	0.8929,	0.8619,	0.7974,	0.6737,	0.4293,	0.3648,	0.5331,	0.2413,	0.5070,	0.8533,	0.6036,	0.8514,	0.8512,	0.5045,	0.1862,	0.2709,	0.4232,	0.3043,	0.6116,	0.6756,	0.5375,	0.4719,	0.4647,	0.2587,	0.2129,	0.2222,	0.2111,	0.0176,	0.1348,	0.0744,	0.0130,	0.0106,	0.0033,	0.0232,	0.0166,	0.0095,	0.0180, 0.0244,	0.0316,	0.0164,0.0095,0.0078)
input_data_as_numpy_array = np.asarray(input_data)

#reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]=='R'):
  print('The object is a rock')
else:
  print('The object is a mine')