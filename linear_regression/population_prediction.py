import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('C:\\Users\\saket\\Downloads\\WPP2019_TotalPopulationBySex.csv')
# print(df.head())

population_per_year = df.groupby('Time').PopTotal.mean().reset_index()
# print(prod_per_year)

x = population_per_year['Time']
x = x.values.reshape(-1, 1)
#print(x)

y = population_per_year['PopTotal']
y = y.values.reshape(-1, 1)
#print(y)

plt.plot(x, y, 'o')
plt.show()