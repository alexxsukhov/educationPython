# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd

data = pd.read_csv('california_housing_test.csv')

print(data[data['population'] == data['population'].min()]['households'].max())
