class HashTable:
    def __init__(self,size = 7):
        self.data_map = [None] * size

    def __hash(self,key):
        my_hash = 0
        for l in key:
            my_hash = (my_hash + ord(l) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i, ": ",val)

    def set_item(self,key,value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self,key):
        index = self.__hash(key)
        if self.data_map[index]is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
        return None

    def key(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


    

my_hash_table = HashTable()

my_hash_table.set_item('bolts',1400)
my_hash_table.set_item('nails',140)
my_hash_table.set_item('washers',400)



print(my_hash_table.key())


# my_hash_table.print_table()