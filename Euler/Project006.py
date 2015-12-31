import numpy as np

x = np.array(range(101))

sum_squares = sum(x**2)
squared_sum = sum(x)**2
print squared_sum - sum_squares
