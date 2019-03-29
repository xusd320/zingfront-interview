class node():
    def __init__(self, val = None, left = None, right = None):
        self.val   = val
        self.left  = left
        self.right = right

def matrixTree(matrix):
    if len(matrix) == 0:
        raise Exception('Empty matrix')
    elif len(matrix[0]) == 0:
        raise Exception('Empty matrix')
    m = len(matrix)
    n = len(matrix[0])

    root = node({'x' : 0, 'y' : 0, 'data' : matrix[0][0]})
    def genTree(root):
        x,y = root.val['x'], root.val['y']
        if x < m -1 and y < n -1:
            root.left  = node(
                val   = {'x' : x + 1, 'y' : y, 'data' :  matrix[x + 1][y]}, 
                left  = genTree(node(val = { 'x' : x + 2, 'y' : y, 'data' : matrix[x + 2][y]})) if x < m -2 else None,
                right = genTree(node(val = { 'x' : x + 1, 'y' : y + 1, 'data' : matrix[x + 1][y + 1] })) 
            )
            
            root.right= node(
                val   = {'x' : x, 'y' : y + 1, 'data' :  matrix[x][y + 1]}, 
                left  = genTree(node(val = { 'x' : x + 1, 'y' : y + 1, 'data' : matrix[x + 1][y + 1] })),
                right = genTree(node(val = { 'x' : x, 'y' : y + 2, 'data' : matrix[x][y + 2]})) if y < n -2 else None
            )

            return root

        elif x < m -1:
            root.left  = node(
                val   = {'x' : x + 1, 'y' : y, 'data' :  matrix[x + 1][y]},
                left  = genTree(node(val = { 'x' : x + 2, 'y' : y, 'data' : matrix[x + 2][y]})) if x < m -2 else None,
            )

            return root

        elif y < n -1:
            root.right= node(
                val   = {'x' : x, 'y' : y + 1, 'data' :  matrix[x][y + 1]},
                right = genTree(node(val = { 'x' : x, 'y' : y + 2, 'data' : matrix[x][y + 2]})) if y < n -2 else None
            )

            return root

        else: 
           
            return node({'x' : x, 'y' : y, 'data' : matrix[x][y]})

    return genTree(root)

'''    
def btreepaths(root):
    if not root:
        return []
    res, stack = [], [(root, [])]
    while stack:
        node, ls = stack.pop()
        if sum(map(lambda item : item['data'], ls)) <= - node.val['data']:
            continue
        if not node.left and not node.right:
            res.append(ls + [node.val])
        if node.left:
            stack.append((node.left, ls + [ node.val ]))
        if node.right:
            stack.append((node.right, ls + [ node.val ]))
            continue
    return res

a = [[1,1,2],[1,2,4], [-1, -2,1]]
tree = matrixTree(a)
print(btreepaths(tree))
'''
