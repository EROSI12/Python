from turtle import pd

import numpy as np

arr_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr_2d)

element = arr_2d[1,2]
print(element)

# pip install numpy

import pandas as pd

product = ['apple', 'oranges', 'tangerine', 'pears']
sales = [150, 200, 350, 90]


sales_series = pd.Series(sales, index=product)


total_sales = sales_series.sum()


print(total_sales)
