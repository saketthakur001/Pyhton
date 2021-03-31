import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

days = np.array(range(1, 101))
days = days.reshape(-1, 1)
data = []
for i in range()

print(len(data), len(days))
line_fitter = LinearRegression()
line_fitter.fit(days, data)
data_predict = line_fitter.predict(days)
plt.plot(days, data, 'o')
plt.plot(days, data_predict)
plt.show()