import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv("../consumo_cerveja.csv",sep=";")

x = df[['temp_max']]
y = df[['consumo']]

X_train, X_test, y_train, y_test = train_test_split(x, y)

lr = LinearRegression().fit(X_train, y_train)

y_pred = lr.predict(X_test)
x_pred = lr.predict(y_test)
val2   = zip(x_pred,y_pred)

vals = zip(y_pred, y_test.values)

plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred, color="blue", linewidth=3)

plt.show()










