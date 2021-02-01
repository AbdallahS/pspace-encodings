# from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import sys
import re

# For naive encoding

x, y = [], []
with open(sys.argv[1], "r") as file:
    for line in file:
        if re.search("SAT", line):
            print(line, end="")
        elif re.search("real", line):
            y.append(re.search(".m.*s$", line).group(0))
        elif re.search("# Vertex", line):
            num = int(re.search("# Vertex:.", line).group(0)[9:])
            x.append(num)
        else:
            print("Error", file=sys.stderr)

plt.scatter(x, y)
plt.xlabel("Number of Vertices")
plt.ylabel("Time")
plt.tight_layout()
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.savefig("graph-instances/naive_vertex.png")
