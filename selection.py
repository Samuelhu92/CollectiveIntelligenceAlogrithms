def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

def binary_search(a_list, item):
    low = 0
    high = len(a_list)-1
    found = False
    while low <= last and not found:
        m = (low+high)/2
        if item == a_list[m]:
            found = True
        else:
            if item < a_list[m]:
                high = m-1
            else:
                low = m+1
    return found

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots =[None]*self.size
        self.data = [None]*self.size

    # put data into slot
    def put_data_in_slot(self, key, data, slot):
        if self.slots[slot] == None:
            self.slots[slot] == key
            self.data[slot] = data
            return True
        else:
            if self.slots[slot] == key:
                sel.data[slot] == data
                return True
            else:
                return False

    def put(self, key, data):
        self.slot = self.hash_function(key,self.size)
        result = self.put_data_in_slot(key,data,slot)
        while not result:
            self.slot = self.rehash(key, self.size)
            result = self.put_data_in_slot(key, data, slot)

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash+1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position =  start_slot
        while self.slots[position] != None and not stop and not found:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = rehash(key, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
        


