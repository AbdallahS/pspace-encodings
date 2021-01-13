########################################################
# Generate_test.py
# Generates test file for available problems
# 13/01/2021
########################################################

########################################################
# Globals
########################################################

intro = '''
What test file would you like to create?

1: vertex-cover
2: Sudoku

Input:'''
vertex_instruction = '''
Print edges in CSV format. For example, an edge between vertex 4 and 5
should be denoted as 4-5. 
Example input: 4-5,6-3,5-4 

Input:'''
options = ['1', '2']

########################################################
# Logic
########################################################

# Choose problem type
print(intro, end=" ")
while True:
    ans = input()
    if ans in options:
        break
    else:
        print("\nInvalid option. Try again:", end=" ")
print("\nType name of file (without extension):", end=" ")
name = input()

# If vertex-cover:
if ans == '1':
    print("Input number of verticies required:", end=" ")
    num_vertex = input()
    print(vertex_instruction, end=" ")
    print("Writing file in test-instances/graph-instances")
    new_file = open(f"test-instances/graph-instances/{name}.bul", "w")  

# %%%%not over-budget. k=3
# %vertex[A], vertex[B], vertex[C], vertex[D], A < B, B < C, C < D :: ~s(A), ~s(B), ~s(C), ~s(D).
# %%%%budget 4
# vertex[A], vertex[B], vertex[C], vertex[D], vertex[E], A < B, B < C, C < D, D < E :: ~s(A), ~s(B), ~s(C), ~s(D), ~s(E).
# %dom[Z] :: q(Y,Z) : dom[Y].