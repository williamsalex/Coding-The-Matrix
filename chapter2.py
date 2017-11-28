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
            for z in voting_dict[X][1:]:
                x=0
                x+=voting_dict[X][z]*f[z]
                if x>a[1]:
                    a=[X,x]
    return a[0]

def listintake(listofstring):
    f = []
    for X in listofstring:
        X.replace(' ', ',')
        f.append(X)
    return(f)

for X in s:
    X.replace(' ', ',')

def least_similar(sen, voting_dict):
        f = voting_dict[sen]
        a = [sen,0]
        for X in voting_dict.keys():
            if X!=sen:
                for z in voting_dict[X][1:]:
                    x=0
                    x+=voting_dict[X][z]*f[z]
                    if x<a[1]:
                        a=[X,x]
        return a[0]

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

# non working
def sen_set(voting_dict, condition):
    s = []
    for X in voting_dict:
        if 'condition' in X:
            s.append(X)
    return create_voting_dict(s)
# non working

def find_average_record(sen_set, voting_dict):
    f = sen_set[0]
    a = 0
    for X in sen_set():
        if X!=sen_set[0]:
            for z in sen_set[X][1:]:
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
