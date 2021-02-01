#!/usr/bin/env python3

########################################################
# budget
# Generate and output budget constraint (in bule encoding) 
# to standard output
# 16/01/2021
########################################################

########################################################
# Imports
########################################################

import sys

########################################################
# Logic
########################################################

# If incorrect number of commndline arguments given, exit
if len(sys.argv) != 2:
    print("Usage: ./budget BUDGET")
    exit()

# Generate budget constraint bule encoding
budget = int(sys.argv[1]) + 1
print(f'% Rule for budget constraints (budget = {budget - 1})')
for i in range(1, budget + 1):
    print(f'vertex[V{i}], ', end="")
print(f'\n    ', end="")
for i in range(1, budget - 1):
    print(f'V{i} < V{i + 1}, ', end="")
print(f'V{budget - 1} < V{budget} ::\n    ', end="")
for i in range(1, budget):
    print(f'~s(V{i}), ', end="")
print(f'~s(V{budget}).\n', end="") 