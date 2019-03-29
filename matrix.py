class Chess():
    def __init__(self, board):
        #初始化棋盘
        if len(board) == 0 :
            raise Exception('Empty borad')
        elif len(board[0]) == 0 :
            raise Exception('Empty borad')

        self.board  =  board
        self.m      = len(board)
        self.n      = len(board[0])

    def searchRound(self, x, y, string):
        hit = True
        while len(string) > 0 and hit:
            #取出string第一个字符，并将剩余赋给string
            s, string = string[0], string[1:]
            #以(x,y)为中心，在周围的8个字符中寻找字符s,若找不到，说明此查找路径走不通,直到string中所有字符命中
            for i in range(x-1, x + 2):
                for j in range(y -1, y + 2):
                    #防止找到(x,y)自生和越出期盼边界
                    if not (i == x and j == y) and i in range(self.m) and j in range(self.n):
                        if self.board[i][j] == s:
                            hit = True
                            return self.searchRound(i,j,string)
                        else:
                            hit = False 
        
        return hit

    def canGenerate(self, string):
        #在棋盘外层包裹一层节点，以保证棋盘边界能被遍历到
        for i in range(-1, self.m + 1):
            for j in range(-1, self.n + 1):
                if self.searchRound(i, j, string):
                    return True
        return False

c = Chess([['A', 'R', 'E'], ['I', 'P', 'D'], ['E', 'L', 'P']])

targets = ['ARE', 'PENPIEAPPLE', 'APPLEPEN', 'APPLE','LIPS', 'RED', 'AIR', 'PLEASE']
for t in targets:
    if c.canGenerate(t):
        print(t)
