import numpy as np
import math
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import random

x = np.array([-3, -2, -1, 0, 1, 2, 3]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1])

# fit the model
model = LogisticRegression().fit(x, y)

# test data
new_x = np.array([-13, -0.5, 1, 0.3, -5, 11, 12]).reshape(-1, 1)
new_y = np.array([0, 0, 1, 1, 0, 1, 1])

# predict
print(model.predict(new_x))

# score the model
print(model.score(new_x, new_y))

plt.scatter(new_x, new_y, color="blue", alpha=0.5)
plt.scatter(new_x, model.predict(new_x), color="red", alpha=0.5)
logx = np.linspace(-13, 12, 100)
logy = 1/(1+math.e**-logx)
plt.plot(logx, logy)
# plt.show()

from sklearn.datasets import load_iris
X, y = load_iris(return_X_y = True)
print(y)
print(X[0:10])
print("...")
print(X[-10:])

# imports for preprocessing
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

# create normalized x values
xscaler = preprocessing.StandardScaler().fit(X)
xscaled = xscaler.transform(X)

# create training/test datasets
x_train, x_test, y_train, y_test = train_test_split(xscaled, y, test_size=0.2, random_state=1)

# create model
model = LogisticRegression(multi_class="multinomial", random_state=1).fit(x_train, y_train)

# test model
print(model.score(x_test, y_test))

# let's take a look at the predictions
print(y_test)
print(model.predict(x_test))