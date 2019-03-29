#利用hash实现简单的set
class MySet():
    def __init__(self, size = 10000):
        self.hash_list = [None for _ in range(size)]
        #index对size取余防止越界
        self.size      = size

    #判断元素是否已存在 
    def exist(self, Str):
        index = hash(Str) % self.size
        return not self.hash_list[index] is None

    #插入新元素
    def put(self, Str):
        index = hash(Str) % self.size
        #若已存在则抛错
        if self.hash_list[index] :
            raise Exception('existed')
        self.hash_list[index] = Str


