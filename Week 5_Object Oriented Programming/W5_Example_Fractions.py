class fraction(object):

    def __init__(self, numer, denom):
        self.denom = denom
        self.numer = numer

    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)

    def getNumer(self):
        return self.numer

    def getDenom(self):
        return self.denom

    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
                   + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)

    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
                   - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)

    def convert(self):
        self.denom -= 1
        return self.denom

a = fraction(1, 3)
b = fraction(2, 3)
print(a.getNumer())

