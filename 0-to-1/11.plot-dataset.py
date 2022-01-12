import random
import matplotlib.pyplot as plt
# can be also written as
# from matplotlib import pyplot as plt

xs = [random.randint(0,10) for _ in range(100)]
ys = [random.randint(0,10) for _ in range(100)]

plt.scatter(xs, ys)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("scatter plot with random int")
plt.show()
