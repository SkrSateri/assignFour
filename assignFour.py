key = input("Please enter your key >")
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#print(len(key))
matrix = []

def add_to_matrix(keyLetter):# To add the letter to the matrix depending on the result of check_matrix function
    if check_matrix(keyLetter):
        matrix.append(keyLetter)

def check_matrix(keyLetter):
    appendable = True
    for x in matrix:
        if x == keyLetter:
            appendable = False
            break
    return appendable

def conver_to_multiverse_list(list):
    indexKeeper = 0
    n = 5
    multiMatrix = [['E' for _ in range(n)] for _ in range(n)]
    for x in range(5):
        for y in range(5):
            multiMatrix[x][y] = list[indexKeeper]
            indexKeeper = indexKeeper + 1
    print_multi_matrix(multiMatrix)

def print_multi_matrix(mm):
    line = ""
    for x in range(5):
        line = ""
        for y in range(5):
            line = line + " " + mm[x][y]
        print(line)

for y in key:
    add_to_matrix(y.upper())
for y in alphabet:
    add_to_matrix(y.upper())

conver_to_multiverse_list(matrix)