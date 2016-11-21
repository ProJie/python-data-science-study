import numpy as np

height = np.round(np.random.normal(175, 30, 5000), 2)
weight = np.round(np.random.normal(175, 30, 5000), 2)
array_2 = np.array([height, weight])
np_city = np.column_stack((height, weight))
print(np_city)
