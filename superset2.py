from MyDict import MyDict

def isSuperSet(A,B):
    d1 = MyDict()
    d2 = MyDict()

    for a in A :
        d1[a] = d1.get(a, 0) + 1

    for b in B :
        d2[b] = d2.get(b, 0) + 1

    for key in d2.keys():
        if d2[key] > d1.get(key, 0):
            return False

    return True



print(isSuperSet('abbccdd', 'abcdd'))
print(isSuperSet('abbcdd', 'abcdd'))
print(isSuperSet('abbccd', 'abcdd'))
