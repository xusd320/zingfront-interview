#利用hash构造简单的dict
class MyDict():
    def __init__(self, size = 100000):
        #以一个二元数据存储[key, value]
        self.hash_list = [list() for _ in range(size)]
        #对size取余防止越界
        self.size      = size

    def __setitem__(self, key, value):
        #利用hash计算key的键位
        hashed_key = hash(key) % self.size
        #若hash_list该键位已有值，则重新设置，若无，则追加该键位
        for item in self.hash_list[hashed_key]:
            if item[0] == key:
                item[1] = value
                break
        else:
            self.hash_list[hashed_key].append([key,value])

    def __getitem__(self, key):
        #计算key的键位并取值，取不到就抛错
        for item in self.hash_list[hash(key) % self.size]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def get(self, key, default):
        #计算key的键位并取值，取不到就返回default
        for item in self.hash_list[hash(key) % self.size]:
            if item[0] == key:
                return item[1]
        return default

