import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# x1 = np.random.poisson(lam=4, size=198)
# x = np.random.normal(loc=4, scale=0.5, size=198)
# for i in range(len(x)):
#     if x[i] > 6 or x[i] <= 0:
#         x[i] = 4
#     print(x[i], end=' ')

# Generate Distribution:
randomNums = np.random.normal(loc=3.5, scale=5.1, size=763)
randomInts = np.round(randomNums)
result = [int(i) for i in randomInts]

for i in range(len(result)):
    if 7 < result[i] < 10:
        result[i] = np.random.randint(5, 8)
    elif 0 >= result[i] >= -3:
        result[i] = np.random.randint(1, 2)
    elif result[i] < -3:
        result[i] = np.random.randint(4, 8)
    elif result[i] >= 10:
        result[i] = np.random.randint(6, 8)
    print(result[i], end=' ')

x = np.arange(start=min(result) - 1, stop=max(result) + 2)
plt.hist(result, bins=x)
plt.show()
