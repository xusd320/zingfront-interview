from MySet import MySet

def isSuperSet(A, B):
    #构造set
    s = MySet(100)
    for i in B :
        #跳过重复元素，防止重复计算
        if  s.exist(i):
            continue 
        else:
           #B中i数量大于A中i数量,则A一定不为B的超集,结束循环
           if B.count(i) - A.count(i) > 0:
               return False
           #i放入set中
           s.put(i) 

    return True


print(isSuperSet('abbccdd', 'abcdd'))
print(isSuperSet('abbcdd', 'abcdd'))
print(isSuperSet('abbccd', 'abcdd'))
