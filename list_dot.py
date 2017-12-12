def list_dot(u,v):
    '''
    >>> list_dot([1,2,8],[3,4,5])
    51

    computes the dot product of two input vectors formatted as lists
    '''
    assert isinstance(u, list) & isinstance(v, list)
    assert len(u) == len(v)
    return sum([X*Y for (X,Y) in  zip(u,v)])
