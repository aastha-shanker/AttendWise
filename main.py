import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Load the dataset
data = pd.read_csv('students_attendance.csv')

maths = data['Maths']
ds = data['DS']
toc = data['TOC']
dbms = data['DBMS']
java = data['Java']

#given credits for each subject
credits = {
  "maths": 4,
  "ds": 3,
  "toc": 3,
  "dbms": 2,
  "java": 2
}

aggregate = (maths*credits['maths'] + ds*credits['ds'] + toc*credits['toc'] + dbms*credits['dbms'] + java*credits['java']) / sum(credits.values())

data['aggregate'] = aggregate
    
data['eligible'] = data['aggregate'].apply(lambda x: 1 if x >= 75 else 0)

print(data.isnull().sum())
 
x = data[['Maths', 'DS', 'TOC', 'DBMS', 'Java' , 'aggregate']]
y = data['eligible']

x_train, x_test , y_train , y_test = train_test_split(x, y, test_size= 0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print("====accuracy_score====")
print(accuracy_score(y_test, y_pred))

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Saved Successfully!")

