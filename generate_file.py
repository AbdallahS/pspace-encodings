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
% Rules for covering edges
edge[U, V] :: s(U), s(V).\n
'''

sudoku_template = '''\
%%% Bule rules for Sudoku game

% Set up domain for Sudoku board 
dom[1..9].
boxOffset[0..2,0..2].
boxBegin[1,1]. boxBegin[1,4]. boxBegin[1,7]. boxBegin[4,1]. boxBegin[4,4]. 
boxBegin[4,7]. boxBegin[7,1]. boxBegin[7,4]. boxBegin[7,7].

%% Game rules
% in every cell at least 1 val
dom[X], dom[Y] :: q(X,Y,Z) : dom[Z].

% Each val in at least 1 cell
dom[Z] :: q(X,Y,Z) : dom[X] : dom[Y].

% Each cell contains no more than 1 val
dom[X],dom[Y], dom[Z1], dom[Z2], Z1 < Z2 :: ~q(X,Y,Z1), ~q(X,Y,Z2). 

% No two same vals in a column
dom[X1], dom[X2], X1 < X2 :: ~q(X1,Y,Z), ~q(X2,Y,Z).

% No two same vals in a row
%dom[Y1], dom[Y2], Y1 < Y2 :: ~q(X,Y1,Z), ~q(X,Y2,Z).

% No two same vals in a single box.
% Note that we do not need the rules for X1==X2 (or Y1==Y2) because they are
% implied by 30 (or 27 respectively)
boxBegin[ROOTX,ROOTY], boxOffset[X1,Y1], boxOffset[X2,Y2], X1<X2, Y1!=Y2
	:: ~q(ROOTX+X1,ROOTY+Y1,Z), ~q(ROOTX+X2,ROOTY+Y2,Z).
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
      new_file.write("\n")
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

def write_sudoku(name):
  with open(f"sudoku/{name}.bul", "w") as new_file:
    new_file.write(sudoku_template)

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

elif ans == '2':
  write_sudoku('test')