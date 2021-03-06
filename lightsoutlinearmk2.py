matrices = [[X for X in [0,1]]]

def possiblePresses(gridsize):
    numberOfButtons = gridsize**2
    subs = subsets(numberOfButtons)
    return [X for X in subs]


def subsets(i):
    if i == 0:
        return[[]]
    else:
        return induct(subsets(i-1),i)


def induct(listoflists,n):
    return listoflists + [X+[n] for X in listoflists]


def createMatrices(dimension):
    matrices = [[]]


Matrix(2,2,[1,0,0,1])

Matrix(2,2,[0,1,1,1])
Matrix(2,2,[1,0,1,1])
Matrix(2,2,[1,1,0,1])
Matrix(2,2,[1,1,1,0])


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
