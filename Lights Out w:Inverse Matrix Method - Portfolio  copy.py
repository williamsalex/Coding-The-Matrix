#This function takes a board size and initial state and returns the solution to the puzzle
#Instead of using brute force, this method utilizes an inverted matrix method

from sympy import Matrix

# Contract : int, list of int -> list
# Purpose : To take an initial game state and grid size and output a series of buttons which, after pressed, will solve the game.
# Example linearLightsOut(2, [0,0,1,1]) : [(0, 0), (0, 1)], linearLightsOut(3, [0,0,1,1,1,0,0,1,0]) : [(0, 0), (0, 2), (1, 1), (2, 2)]
def linearLightsOut(gridsize, initial):
    grid = [(X,Y) for X in range(0, gridsize, 1) for Y in range(0, gridsize, 1)]
    buttonAffect = []
    for Y in grid:
        buttonAffect.append(translator(pressAffect(Y, gridsize),gridsize))
    vectorlist = []
    for X in range(0,gridsize**4,1):
        vectorlist.append(0)
    for Z in range(0,len(buttonAffect),1):
        for X in buttonAffect[Z]:
            vectorlist[X-1+gridsize**2*Z] = 1
    Y=0
    L=[]
    for X in Matrix(gridsize**2,gridsize**2, vectorlist).inv_mod(2).LUsolve(Matrix(initial)):
        Y=Y+1
        if(int(str(X).split('/')[0])%2 == 1):
            L.append(Y)
    return reverseTranslator(L,gridsize)

#Functions re-used from Lights Out Problem - Portfolio

def pressAffect(button, domain):
    x1 = ((button[0]-1), button[1])
    x2 = ((button[0]+1), button[1])
    y1 = (button[0], (button[1]-1))
    y2 = (button[0], (button[1]+1))
    affected = [x1, x2, y1, y2, button]
    return [x for x in affected if (x[0] < domain and x[1] < domain and x[0] >= 0 and x[1] >= 0)]

def translator(list,gridsize):
    coordinates = [(X,Y) for X in range(gridsize) for Y in range(gridsize)]
    numbers = range(1,gridsize**2+1,1)
    converter = {value:key for (key,value) in zip(numbers, coordinates)}
    return [converter[x] for x in list]

def reverseTranslator(list,gridsize):
    coordinates = [(X,Y) for X in range(gridsize) for Y in range(gridsize)]
    numbers = range(1,gridsize**2+1,1)
    converter = {key:value for (key,value) in zip(numbers, coordinates)}
    return [converter[x] for x in list]
