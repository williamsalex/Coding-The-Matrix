import doctest
from pydoc import help


# Contract list_dot : list, list -> int
# Purpose to compute the dot product of two input vectors formatted as lists
# Example list_dot([1,3,5],[2,4,6]) should produce 44
def list_dot(u,v):
    '''
    >>> list_dot([1,2,8],[3,4,5])
    51

    computes the dot product of two input vectors formatted as lists'''

    return sum([X*Y for (X,Y) in  zip(u,v)])

# Contract listintake : textwrapper -> dictionary
# Purpose to take the raw data in the file and process it so it is in a dictionary format
# Example listintake(open('voting_record_dump109.txt')) -> {'Burns': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'Obama': [1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1], etc..
def listintake(votingrecord):
    '''
    takes in raw data and refines it into a dictionary form
    '''
    splitstring=[]
    for X in votingrecord:
        splitstring.append(X.split())
    x = {}
    for X in splitstring:
            x.update({X[0]:[int(f) for f in X[3:]]})
    return x

# outdated function
def create_voting_dict(strlist):
    x = {}
    for X in strlist:
            x.update({X[0]:[int(f) for f in X[3:]]})
    return x

# Contract policy_compare : string, string, dict -> int
# Purpose to compute the dot product of the two senators records, showing how similar their positions are
# Example policy_compare('Akaka', 'Obama', f2) -> 34
def policy_compare(sen_a, sen_b, voting_dict):
    '''
    takes in two senators and a voting record and shows how similar their positions overall were
    '''
    f = 0
    for X in range(0,len(voting_dict[sen_a]),1):
            f+=voting_dict[sen_a][X]*voting_dict[sen_b][X]
    return f

# Contract find_average_similarity : string, list of strings, dict
# Purpose to show how similar one senator is to a set of other senators
# Example find_average_similarity('Akaka', republicans, f2) -> -33.278688524590166
def find_average_similarity(sen, sen_set, voting_dict):
    '''
    returns how similar the senator is to the set of senators
    '''
    f = voting_dict[sen]
    a = 0
    for X in sen_set.keys():
        if X!=sen:
            for z in sen_set[X][1:]:
                a+=sen_set[X][z]*f[z]
    return a/len(sen_set)

# outdated function
def sen_set(voting_dict, condition):
    s = []
    for X in voting_dict:
        for Y in X:
            if condition in Y:
                s.append(X[:3]+[int(X) for X in X[3:]])
    x = {}
    for X in s:
        x.update({X[0]:[f for f in X[3:]]})
    return x

# Contract least_similar : string, dict -> list
# Purpose to output the name of the senator who opposes the input senator on the most issues
# Example least_similar('Akaka', f2) -> ['Sununu', 1]
def least_similar(sen, voting_dict):
    '''
    returns the senator who is least similar to the input
    '''
    f = voting_dict[sen]
    a = [sen,list(voting_dict)[0]]
    for X in voting_dict.keys():
        if X!=sen:
            x=0
            x=list_dot(voting_dict[sen], voting_dict[X])
            print(x)
            if x<a[1]:
                a = [X, x]
    return a

# Contract most_similar : string, dict -> list
# Purpose to output the name of the senator who agrees with the input senator on the most issues
# Example most_similar('Akaka', f2) -> ['Kennedy', 43]
def most_similar(sen, voting_dict):
    '''
    returns the senator who is most similar to the input
    '''
    f = voting_dict[sen]
    a = [sen, list(voting_dict)[0]]
    for X in voting_dict.keys():
        if X!=sen:
            x=0
            x=list_dot(voting_dict[sen], voting_dict[X])
            print(x)
            if x>a[1]:
                a = [X, x]
    return a

# Contract bitter_rivals : dict -> string
# Purpose to output the names of the two most opposed senators
# Example bitter_rivals(f2) -> 'Inhofe and Feingold'
def bitter_rivals(voting_dict):
    '''
    outputs the senators who oppose eachother the most
    '''
    a = [0,0]
    f = [0,0]
    b = ""
    for X in voting_dict.keys():
        f = least_similar(X, voting_dict)
        if f[1]<a[1]:
            a=f
            b=X
    return str(a[0])+" and "+b

# Contract find_average_record set, dict -> list
# Purpose to show the average record of the senators among the input set
# Example find_average_record(republicans, f2) -> [54, 46, 62, 62, 62, 56, 40, 51, 62, 18, 44, -5, 47, 57, 30, 54, 59, 58, 40, 59, 62, 62, 62, -12, 30, 60, 46, 58, 60, 56, 51, 61, 58, 61, 61, 41, 60, 51, 56, 60, 60, 57, 40, 61, 62, 44]
def find_average_record(sen_set, voting_dict):
    '''
    finds the average record of the set of input senators
    '''
    total = voting_dict[list(sen_set)[0]][:]
    for X in list(sen_set):
        if X != list(sen_set)[0]:
            for Y in range(len(total)):
                total[Y] = total[Y]+voting_dict[X][Y]
    for X in range(len(total)):
        total[X] = total[X]/len(sen_set)
    return total
