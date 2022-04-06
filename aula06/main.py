import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_excel("../expectativa.xlsx")

x = df[['Expectativa']]
y = df[['idh']]

X_train, X_test, y_train, y_test = train_test_split(x, y)

lr = LinearRegression().fit(X_train, y_train)

preds = lr.predict(X_test)

for a in zip(preds, y_test.values):
    print(a)