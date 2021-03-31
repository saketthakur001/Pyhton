import pandas as pd
from sklearn.model_selection import train_test_split

location = 'D:\\PYTHON\\1python_py_files\\1.PROJECTS\\multiple linear regression\\'
streeteasy = pd.read_csv(location + 'manhattan.csv')
df = pd.DataFrame(streeteasy)
#print(df)

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]
y = df['rent']

x_train 