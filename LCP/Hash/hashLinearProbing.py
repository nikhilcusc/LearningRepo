

class HashMap:
    def __init__(self,s):
        self.size = s
        self.map = [None] * self.size
    
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash%self.size

    def add(self, key, value):

        key_hash = self._get_hash(key)
        key_value = [key,value]

        if self.map[key_hash] is None:

            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] == value
                    return True

            self.map[key_hash].append(key_value)
            return True
        
    def get(self, key):
        hash1 = self._get_hash(key)

        if self.map[hash1] is not None:
            for pair in self.map[hash1]:
                if pair[0] == key:
                    return pair[1]
        return None
    

    def delete(self, key):
        hash1 = self._get_hash(key)
        if self.map[hash1] is None:
            return False
        for i in range (0,len(self.map[hash1])):
            if self.map[hash1][i][0] == key:
                self.map[hash1].pop(i)
                return True

    def print(self):
        for i in self.map:
            if i is not None:
                print(str(i))


h = HashMap(6)
h.add('B','325223')
h.add('Bs','532523')
h.add('Bs','966342')
h.add('Aad','5345677')
h.add('aer','234856')
h.add('Mil','7844389')

h.print()

h.delete('B')
h.print()
print('Mil : '+ h.get('Mil'))

