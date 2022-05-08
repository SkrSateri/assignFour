key = input("Please enter your key >")
alphabet = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#print(len(key))
matrix = []
fiveDMatrix = [['E' for _ in range(5)] for _ in range(5)]
exitApplication = False
operation = 0
plainInput = ""

def add_to_matrix(keyLetter):# To add the letter to the matrix depending on the result of check_matrix function
    if check_matrix(keyLetter):
        matrix.append(keyLetter)

def check_matrix(keyLetter):# To check if the matrix already has that letter or not
    appendable = True
    for x in matrix:
        if x == keyLetter:
            appendable = False
            break
    return appendable

def conver_to_multiverse_list(list):# To convert one dimentional letter into 5 dimentional letter
    indexKeeper = 0
    n = 5
    multiMatrix = [['E' for _ in range(n)] for _ in range(n)]
    for x in range(5):
        for y in range(5):
            multiMatrix[x][y] = list[indexKeeper]
            indexKeeper = indexKeeper + 1
    return multiMatrix

def print_multi_matrix(mm):# To print multidimentional matrix on the console
    line = ""
    for x in range(5):
        line = ""
        for y in range(5):
            line = line + " " + mm[x][y]
        print(line)

def get_letter_multi_index():# To get a letter's index in multidim. matrix
    row = 0
    column = 0
    row = int(matrix.index("Z")/5)
    column = matrix.index("Z")%5

def init_matrix(k):# to initialise one dinensional matrix to use in decyription and encryption
    k = convert_key(k)
    for y in k:
        add_to_matrix(y.upper())
    for y in alphabet:
        add_to_matrix(y.upper())

def convert_key(plainI):# This function is going to convert a key into a workable input,(removing spaces, changing letter j with i ...etc).
    workableT = ""
    for x in plainI:
        if x.upper() == "J":
            workableT = workableT + "I"
        elif x != x.upper():
            workableT = workableT + x.upper()
    print(workableT)
    return workableT

def convert_plain_input(plainI):# This function is going to convert a plain input into a workable input,(removing spaces, changing letter j with i ...etc).
    workableT = ""
    tempText = ""
    isLettersSame = False
    indexTracker = 0
    plainILength = len(plainI)
    #first convertion rule for changing letter j and 
    #removing numbers + symbols from it
    for x in plainI:
        if x.upper() == "J":
            workableT = workableT + "I"
        elif x != x.upper():
            workableT = workableT + x.upper()
    while (indexTracker < plainILength):
        try:
            twoLetters = workableT[indexTracker] + workableT[indexTracker + 1 ]
            print(twoLetters)
            if twoLetters[0] == twoLetters[1]:
                twoLetters = workableT[indexTracker] + "X"
                tempText = tempText + twoLetters
                indexTracker = indexTracker + 1
            else:
                tempText = tempText + twoLetters
                indexTracker = indexTracker + 2
            twoLetters = ""
        except:
            print("out of list range ")
            twoLetters = workableT[plainILength-1] + "X"
            tempText = tempText + twoLetters
            break
    workableT = tempText
    #print(workableT)
    return workableT
    
def encrypt_plain_input(plainI):
    print("to be continue")

# Main events start from here

init_matrix(key)
fiveDMatrix = conver_to_multiverse_list(matrix)
print_multi_matrix(fiveDMatrix)

while exitApplication == False:
    operation = input("Please choose operation (1) Encrypt (2) De-crypt > ")
    plainInput = input("Enter plain input > ")
    plainInput = convert_plain_input(plainInput)
    print(plainInput)
    