class MyDict():
    def __init__(self, size = 100000):
        self.hash_list = [list() for _ in range(size)]
        self.size      = size

    def __setitem__(self, key, value):
        hashed_key = hash(key) % self.size
        for item in self.hash_list[hashed_key]:
            if item[0] == key:
                item[1] = value
                break
        else:
            self.hash_list[hashed_key].append([key,value])

    def __getitem__(self, key):
        for item in self.hash_list[hash(key) % self.size]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def get(self, key, default):
        for item in self.hash_list[hash(key) % self.size]:
            if item[0] == key:
                return item[1]
        return default

