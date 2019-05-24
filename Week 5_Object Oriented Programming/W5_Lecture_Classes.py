# Create a Coordinate class (a new 'type')
class Coordinate(object):
    # Use a special method called __init__ to initialize some data attributes
    # self = parameter to refer to an instance of the class
    # x & y = what data initializes a Coordinate object
    def __init__(self, x, y):
        # When we invoke creation of an instance, this will bind the variables
        # x and u within that instance to the supplied values

        # Two data attributes for every Coordinate object, x and y, which are both instance variables
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    # Python calls the __str__ method when used  with print
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'






# Create an instance of the Coordinate class: 'c'
c = Coordinate(3, 4)

# Create another instance 'origin'
origin = Coordinate(0, 0)


# Use the dot (.) notation to access an attribute of an instance

# c.x is interpreted as getting the value of c (a frame) and then looking up
# the value associated with x within that frame (The specific value for only this instance)
print(c.x)
print(c.y)

print(Coordinate.distance(origin, c))


# Call the distance function to calculate the distance b/n c and origin
# c.distance inherits the distance from the class definition, and automatically uses c as the first argument.
print(c.distance(origin))

# When passed to print, python calls the __str__special method
print(c)
print(str(c))

# Coordinate is a class
print(Coordinate)

print(type(Coordinate))

print(Coordinate, type(Coordinate))

# Check if c is an instance of class 'Coordinate', or if Coordinate is the type of c
print(isinstance(c, Coordinate))



