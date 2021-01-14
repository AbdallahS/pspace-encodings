########################################################
# Generate_test.py
# Generates test file for available problems
# 13/01/2021
########################################################

########################################################
# Imports
########################################################

import math

########################################################
# Globals
########################################################

intro = '''
What test file would you like to create?\n
1: vertex-cover
2: Sudoku\n
Input:'''

vertex_instruction = '''
Print edges in CSV format. For example, an edge between vertex 4 and 5
should be denoted as 4-5. 
Example input: 4-5,6-3,5-4 
\nInput:'''

vertex_intro = f'''\
% Naive vertex-cover encoding\n
% Represent vertex domain and connected edges
'''

options = ['1', '2']
vertex_info = '''
\n% Rules for covering edges
edge[U, V] :: s(U), s(V).\n
'''

########################################################
# Functions
########################################################

def write_vertex(num_vertex, name, budget, cmd):
  with open(f"vertex-cover/{name}.bul", "w") as new_file:
    new_file.write(vertex_intro + f"vertex[1..{num_vertex}].\n")
    for i in range(math.ceil(len(cmd)/4)):
      for i in range(4):
        if len(cmd) <= 0:
          break
        temp = cmd[0].split('-')
        cmd.pop(0)
        new_file.write(f'edge[{temp[0]}, {temp[1]}]. ')
      new_file.write(vertex_info + 
        f'% Rules for budget constraints (budget = {budget - 1})\n')
    for i in range(1, budget + 1):
      new_file.write(f'vertex[V{i}], ')
    new_file.write(f'\n    ')
    for i in range(1, budget - 1):
      new_file.write(f'V{i} < V{i + 1}, ')
    new_file.write(f'V{budget - 1} < V{budget} ::\n    ')
    for i in range(1, budget):
      new_file.write(f'~s(V{i}), ')
    new_file.write(f'~s(V{budget}).\n')

########################################################
# Logic
########################################################

# Choose problem type
print(intro, end=" ")
ans = input()
while ans not in options:
    print("\nInvalid option. Try again:", end=" ")
    ans = input()

# If vertex-cover:
if ans == '1':
  print("\nInput number of verticies (starting from 1):", end=" ")
  num_vertex = int(input())
  print("\nInput budget:", end=" ")
  budget = int(input()) + 1
  if num_vertex <= 1 or num_vertex < budget:
    print("Invalid vertex cover instance")
    exit()
  print(vertex_instruction, end=" ")
  cmd = input().split(',')
  print("\nType name of file (without extension):", end=" ")
  name = input()
  print("\nWriting file in vertex-cover/\n")
  write_vertex(num_vertex, name, budget, cmd)
  print("Done")
# %%%%not over-budget. k=3
# %vertex[A], vertex[B], vertex[C], vertex[D], A < B, B < C, C < D :: ~s(A), ~s(B), ~s(C), ~s(D).
# %%%%budget 4
# vertex[A], vertex[B], vertex[C], vertex[D], vertex[E],
#   A < B, B < C, C < D, D < E ::
#       ~s(A), ~s(B), ~s(C), ~s(D), ~s(E).
# %dom[Z] :: q(Y,Z) : dom[Y].
# Test inpuf: 5 vertex 1-2,3-4,4-5,1-2,2-3
# 1-2,1-3,1-4,1-5,2-3,2-4,2-5,3-4,3-5,4-5
