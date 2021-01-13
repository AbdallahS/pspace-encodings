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
error = "\nInvalid option. Try again:"
instructions = "\nType name of file (without extension):"
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
        print(error, end=" ")
print(instructions, end=" ")
name = input()

# If vertex-cover:
if ans == '1':
    print("Writing file in test-instances/graph-instances")
    new_file = open(f"test-instances/graph-instances/{name}.bul", "w")
