# Create a new type to represent a collection of integers
class intset(object):
    def __init__(self):
        self.vals = []
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def ismember(self, e):
        return e in self.vals
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'


s = intset()

s.insert(3)
s.insert(4)

print(s)
print(s.ismember(3))
print(s.ismember(6))

print(s.remove(3))

