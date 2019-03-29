class Chess():
    def __init__(self, board):
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
            s, string = string[0], string[1:]
            for i in range(x-1, x + 2):
                for j in range(y -1, y + 2):
                    if not (i == x and j == y) and i in range(self.m) and j in range(self.n):
                        if self.board[i][j] == s:
                            hit = True
                            return self.searchRound(i,j,string)
                        else:
                            hit = False 
        
        return hit

    def canGenerate(self, string):
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
