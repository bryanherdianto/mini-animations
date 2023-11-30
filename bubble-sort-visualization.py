import matplotlib.pyplot as plt
import numpy

amount = 10

lst = numpy.random.randint(0, 100, amount)
x = numpy.arange(0, amount, 1)

n = len(lst)
for i in range(n):
    for j in range(0, n - 1 - i):
        plt.bar(x, lst)
        plt.pause(0.001)
        plt.clf()
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

plt.show()