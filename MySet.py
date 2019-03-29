class MySet():
    def __init__(self, size = 10000):
        self.hash_list = [str() for _ in range(size)]
        self.size      = size

    def exist(self, Str):
        index = hash(Str) % self.size
        return self.hash_list[index] != ''
 
    def put(self, Str):
        index = hash(Str) % self.size
        if self.hash_list[index] :
            raise Exception('existed')
        self.hash_list[index] = Str

