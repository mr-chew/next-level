import numpy as np
import math
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random

arr = [1, 3, 5, 7, 9]
def _func(x):
    return 2 * x + random.uniform(-.1, .1)
x_arr = np.array(arr).reshape(-1, 1)
y_1 = [_func(a) for a in arr]
y_arr = np.array(y_1)

# print(x_arr)
# print(y_arr)

model = LinearRegression().fit(x_arr, y_arr)
# plt.scatter(x_arr, y_arr)
# plt.plot(x_arr, model.predict(x_arr))
# plt.show()

# print(model.coef_)
# print(model.intercept_)

# mse = sum((y_arr - model.predict(x_arr))**2)
# avg_err = math.sqrt(mse/5)
# print(avg_err)

def mse(i, j):
    return sum((i - j)**2)
def avg_err(sum_err, _len):
    return math.sqrt(sum_err/_len)

# arrs = np.genfromtxt("lin_reg_data.csv", delimiter=",", skip_header=0)
# x = arrs[:, 0].reshape(-1, 1)
# y = arrs[:, 1]
# model = LinearRegression().fit(x, y)

# # average error
# _len = y.size
# _avg_err = avg_err(mse(y, model.predict(x)), _len)
# print("The average price error per apartment from this model is", _avg_err)

# # coefficients and intercepts
# print("The linear scaling coefficient for square feet in this model is", model.coef_[0])
# print("The offsetting price/intercept of this model is", model.intercept_)

# # plot
# plt.scatter(x, y)
# plt.plot(x, model.predict(x), color="black")
# plt.show()

arrs = np.genfromtxt("trees.csv", delimiter=",", skip_header=1)
x = arrs[:, 0:2].reshape(-1, 2)
y = arrs[:, 2]
model = LinearRegression().fit(x, y)

x1 = []
x2 = []
for entry in x:
    x1.append(entry[0])
    x2.append(entry[1])
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.scatter(x1, x2, y, alpha=0.3)
ax.plot(x1, x2, model.predict(x), color='black')
# plt.show()
print("Our R squared value is", model.score(x, y))
print(model.coef_)
print(model.intercept_)