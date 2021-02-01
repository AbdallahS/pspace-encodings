# from scipy.stats import norm
# import numpy as np
import matplotlib.pyplot as plt
import os

x_coordinates = [1, 2, 1]
y_coordinates = [4, 5, 2]

plt.scatter(x_coordinates, y_coordinates)

# plt.plot(x, norm.pdf(x))

plt.savefig("result.png")









 # "(time ./test graph-instances/graph1.bul problems/vertex-cover.bul) 2>&1 | grep "real" > temp.txt"



