
class HashTable:
    def __init__(self, size = 7):
        self.map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.map)
        return my_hash

    def print_table(self):
        for idx, val in enumerate(self.map):
            print(idx, ":", val)
    
    def set_item(self, key, value):
        idx = self.__hash(key)
        if self.map[idx] == None:
            self.map[idx] = []
        self.map[idx].append([key, value])
    
    def get_item(self, key):
        idx = self.__hash(key)
        if self.map[idx] is not None:
            for val in self.map[idx]:
                if val[0] == key:
                    return val[1]
        
        return None

    def keys(self):
        key = []
        for val in self.map:
            if val is not None:
                for value in val:
                    key.append(value[0])
        return key


hash = HashTable()

hash.print_table()

print("*****************************")

hash.set_item("AB", 100)
hash.set_item("CD", 200)
hash.set_item("EF", 300)
hash.set_item("GH", 400)
hash.set_item("ABC", 500)
hash.set_item("300", "Sourav")

hash.print_table()

print("*****************************")

value = hash.get_item("AB")
print("Value for AB key is:", value)
value = hash.get_item("CD")
print("Value for CD key is:", value)
value = hash.get_item("EF")
print("Value for EF key is:", value)
value = hash.get_item("GH")
print("Value for GH key is:", value)
value = hash.get_item("ABC")
print("Value for ABC key is:", value)
value = hash.get_item("EFG")
print("Value for EFG key is:", value)

print("*****************************")

keys = hash.keys()

print("Keys present in hashtable: ", keys)