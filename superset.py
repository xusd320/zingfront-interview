from MySet import MySet

def isSuperSet(A, B):
    s = MySet()
    for i in B :
        if  s.exist(i):
            continue 
        elif B.count(i) - A.count(i) > 0:
            return False

    return True


print(isSuperSet('abbccdd', 'abcdd'))
print(isSuperSet('abbcdd', 'abcdd'))
print(isSuperSet('abbccd', 'abcdd'))
