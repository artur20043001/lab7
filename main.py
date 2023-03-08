# 1
import csv
import time
from random import randint

import matplotlib.pyplot as plt
import numpy
import numpy as np
from matplotlib.animation import FuncAnimation

a = [randint(-100000000, 100000000) for i in range(1000000)]
b = [randint(-100000000, 100000000) for i in range(1000000)]
h = []
t_start = time.perf_counter()
for i in range(1000000):
    h.append(a[i] * b[i])
all_time = time.perf_counter() - t_start
print(all_time)
c = np.random.randint(-10000000, 10000000, 1000000)
l = np.random.randint(-10000000, 10000000, 1000000)
t_start = time.perf_counter()
x = numpy.multiply(c, l)
all_time = time.perf_counter() - t_start
print(all_time)
# 2
x1 = []
c = 0
with open('data2.csv', "r") as csvfile:
    table = csv.reader(csvfile, delimiter=",")
    for row in list(table):
        if 0 < c < 18:
            x1.append(float(row[0]))
        if c == 18:
            break
        c += 1
x = np.arange(1, 18)
y = np.array(x1)

fig, ax = plt.subplots()

ax.bar(x, y)

ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)  # ширина Figure
fig.set_figheight(6)  # высота Figure
plt.show()
f_std = np.std(y)
print(np.std(y))
# 3
import math
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# create 3d axes
fig = plt.figure()
ax = plt.axes(projection='3d')

# cordiates for spiral
x = np.linspace(-2 * math.pi, 2 * math.pi, 10000)
z = np.cos(x) * np.sin(x)
y = np.cos(x) * np.sin(x)
ax.plot3D(x, y, z, 'red')

ax.view_init(120, 90)
plt.show()
# additional
fig, ax = plt.subplots()
x = np.arange(0, 4 * np.pi, 0.001)
y = np.sin(x)
line = plt.plot(x, y)
ax.set_title('y = sin(x)')
ax = plt.axis([0, 4 * np.pi, -1.1, 1.1])
dot, = plt.plot([0], [np.sin(0)], 'go')


def func(i):
    dot.set_data(i, np.sin(i))
    return dot,


animation = FuncAnimation(fig, func, frames=np.arange(0, 4 * np.pi, 0.1), interval=100, repeat=True)
plt.show()
