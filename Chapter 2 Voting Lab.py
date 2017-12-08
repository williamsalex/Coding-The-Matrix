def list_dot(u,v):
    return sum([X*Y for (X,Y) in  zip(u,v)])


def create_voting_dict(strlist):
    x = {}
    for X in strlist:
            x.update({X[0]:[int(f) for f in X[2:]]})
    return x

def policy_compare(sen_a, sen_b, voting_dict):
    f = 0
    for X in range(0,len(voting_dict[sen_a]),1):
            f+=voting_dict[sen_a][X]*voting_dict[sen_b][X]
    return f

def most_similar(sen, voting_dict):
    f = voting_dict[sen]
    a = [sen,0]
    for X in voting_dict.keys():
        if X!=sen:
            x=0
            for z in voting_dict[X][1:]:
                x+=voting_dict[X][z]*f[z]
                if x>a[1]:
                    a=[X,x]
    return a

for X in s:
    X.replace(' ', ',')

def least_similar(sen, voting_dict):
    f = voting_dict[sen]
    a = [sen,0]
    for X in voting_dict.keys():
        if X!=sen:
            #for z in range(0,len(voting_dict[X])):
                #x+=voting_dict[X][z]*f[z]
            print(f)
            print(a)
            x=list_dot(f,voting_dict[X])
            print(x)
            if x<a[1]:
                a=[X,x]
    return a

def find_average_similarity(sen, sen_set, voting_dict):
    f = voting_dict[sen]
    a = 0
    for X in sen_set.keys():
        if X!=sen:
            for z in sen_set[X][1:]:
                a+=sen_set[X][z]*f[z]
    return a/len(sen_set)

s = []
for X in voting_dict:
    if ' D ' in X:
        s.append(X)

def listintake(votingrecorddump):
    splitstring=[]
    for X in votingrecorddump:
        splitstring.append(X.split())
    f = []
    for X in splitstring:
        for Y in X[3:]:
            int(Y)
        f.append(X)
    return(f)

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

# non-working

def find_average_record(sen_set, voting_dict):
    f = []
    a = 0
    for X in sen_set.keys():
            for z in sen_set[X]:
                print(z)
                a+=sen_set[X][z]*f[z]
    setavg = a/len(sen_set)
    f = voting_dict[sen]
    a = 0
    for X in voting_dict.keys():
        if X in sen_set:
            break
        else:
            for z in voting_dict[X][1:]:
                a+=voting_dict[X][z]*f[z]
    overallavg = a/len(voting_dict)
    return (setavg/overallavg)*2

# non-working


def least_similar(sen, voting_dict):
    f = voting_dict[sen]
    a = [sen,0]
    for X in voting_dict.keys():
        if X!=sen:
            x=0
            for z in voting_dict[X]:
                x+=voting_dict[X][z]*f[z]
                if x<a[1]:
                    a=[X,x]
    return a

def bitter_rivals(voting_dict):
    a = [0,0]
    f = [0,0]
    b = ""
    for X in voting_dict.keys():
        f = least_similar(X, voting_dict)
        if f[1]<a[1]:
            a=f
            b=X
    return str(a[0])+" and "+b
