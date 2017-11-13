# This function accepts a board size and state for the game Lights Out and outputs the solution to the game.
# Lights Out is a game with a square board, on top of which there is a grid of buttons. When pressed, a button turns either on or off and also switches the state of the buttons around it.
# Lights Out begins with some buttons initially on or off, and it is the job of the player - or function - to figure out how to switch all the states to off.

from GF2 import one
class Vec:
    def __init__(self,labels,function):
        self.D = labels
        self.f = function
# Contract : int, list of tuples -> list of tuples
# Purpose : To take an initial game state and output a series of buttons which, after pressed, will solve the game.
# Example lightsOut(2,[(0,0),(1,1)]) : [[(0, 0), (1, 1)]], lightsOut(3,[(0,1),(1,2)]) : [[(0, 0), (1, 0), (2, 1), (2, 2)]]
def lightsOut(gridsize,Pressedbuttons):
    pointpool=[(X,Y) for X in range(gridsize) for Y in range(gridsize)]
    initial = Vec(pointpool,{button:one for button in Pressedbuttons})
    possiblePress = possiblePresses(gridsize)
    resultvectors = [[buttonPresser(initial, X),X] for X in possiblePress]
    finalresultvectors = [[sparseTrimmer(X[0]), X[1]] for X in resultvectors]
    solution = [X[1] for X in finalresultvectors if X[0].f =={}]
    if solution == [[]]:
        return("No Presses Necessary!")
    else:
        return solution

# Contract : int -> list of lists of tuples
# Purpose : To construct a list of all possible sequences of button presses given a certain size grid.
# Example : possiblePresses(2) : [[], [(0, 0)], [(0, 1)], [(0, 0), (0, 1)], [(1, 0)], [(0, 0), (1, 0)], [(0, 1), (1, 0)], [(0, 0), (0, 1), (1, 0)], [(1, 1)], [(0, 0), (1, 1)], [(0, 1), (1, 1)], [(0, 0), (0, 1), (1, 1)], [(1, 0), (1, 1)], [(0, 0), (1, 0), (1, 1)], [(0, 1), (1, 0), (1, 1)], [(0, 0), (0, 1), (1, 0), (1, 1)]]
def possiblePresses(gridsize):
    numberOfButtons = gridsize**2
    subs = subsets(numberOfButtons)
    return [translator(X,gridsize) for X in subs]

# Contract : list, int -> list
# Purpose : To translate numbered points into points on a coordinate grid.
# Example : translator([1,2,3,4],2) : [(0,0), (0,1), (1,0), (1,1)]
def translator(list,gridsize):
    coordinates = [(X,Y) for X in range(gridsize) for Y in range(gridsize)]
    numbers = range(1,gridsize**2+1,1)
    converter = {key:value for (key,value) in zip(numbers, coordinates)}
    return [converter[x] for x in list]

# Contract : int -> list of lists of ints
# Purpose : To create a list of all possible combinations of the int and all ints less than it.
# Example : subsets(2) : [[], [1], [2], [1,2]], subsets(5) : [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4], [5], [1, 5], [2, 5], [1, 2, 5], [3, 5], [1, 3, 5], [2, 3, 5], [1, 2, 3, 5], [4, 5], [1, 4, 5], [2, 4, 5], [1, 2, 4, 5], [3, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5], [1, 2, 3, 4, 5]]
def subsets(i):
    if i == 0:
        return[[]]
    else:
        return induct(subsets(i-1),i)

# Contract : list of lists, int -> list of lists
# Purpose : To expand a list of coordinates in integer form
# Example : induct([[0,1,2],[0],[],[1,2]],3) : [[0, 1, 2], [0], [], [1, 2], [0, 1, 2, 3], [0, 3], [3], [1, 2, 3]]
def induct(listoflists,n):
    return listoflists + [X+[n] for X in listoflists]

# Contract : vec, list of tuples -> vec
# Purpose : To simulate pressing a series of buttons on the board.
# Example : buttonPresser(Vec({(0,1),(1,0),(0,0),(1,1)}, {(0,1): one, (1,0): 0, (0,0): 0, (1,1): one}), [(0,0),(1,1)]) -> Vec({(0,1),(1,0),(0,0),(1,1)},{(0,1):one, (1,0): 0, (0,0): one, (1,1): 0})
def buttonPresser(initial, buttonpress):
    if buttonpress == []:
        return initial
    else:
        return buttonPresser(SinglebuttonPresser(initial, buttonpress[0]), buttonpress[1:])

# Contract : vec, tuple -> vec
# Purpose : To simulate the effect of pressing a single button on the board.
# Example : SinglebuttonPresser(Vec({(0,0),(1,0),(0,1),(1,1)},{(0,1):one,(0,0):0}), (1,1)) -> Vec({(0,1),(1,0),(0,0),(1,1)},{(0,1):0, (1,0): one, (0,0): 0, (1,1): one})
def SinglebuttonPresser(initial, press):
    return addVector(initial, buttonToVector(press, initial.D))

def getitem(v,d): return v.f[d] if d in v.f else 0

def addVector(a, b):
    return Vec(a.D,{d:getitem(a,d)+getitem(b,d) for d in a.D})

def buttonToVector(button, domain):
    switchedSet = pressAffect(button, domain)
    return Vec(domain,{X:one for X in switchedSet})

# Contract : tuple, set of tuples -> list of tuples
# Purpose : To simulate the affect of the pressing of a button on the board.
# Example : pressAffect((1,1),[(0,0),(1,1),(1,0),(0,1)]) -> [(0, 1), (1, 0), (1, 1)]
def pressAffect(button, domain):
    x1 = ((button[0]-1), button[1])
    x2 = ((button[0]+1), button[1])
    y1 = (button[0], (button[1]-1))
    y2 = (button[0], (button[1]+1))
    affected = [x1, x2, y1, y2, button]
    return [x for x in affected if x in domain]

# Contract : vec -> vec
# Purpose : To take a vector and eliminate the values in the domain which have values of 0, creating a sparse vector.
# Example : sparseTrimmer(Vec({(0,1),(1,0),(0,0),(1,1)}, {(0,1): one, (1,0): 0, (0,0): 0, (1,1): one})) -> Vec({(0,1),(1,0),(0,0),(1,1)}, {(0,1): one, (1,1): one})
def sparseTrimmer(singleVec):
    return Vec(singleVec.D, superSparseTrimmer(singleVec.f))


def superSparseTrimmer(dictionary):
    X={}
    for k,v in (dictionary.items()):
        if v == one:
            X.update({k:v})
    return X
