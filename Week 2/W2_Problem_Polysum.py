import math

def polysum(n, s):
    """This function takes the number (n) and lengths (s) of sides of  a regular polygon and returns
    the sum of its area and the square of its perimeter"""
    def area(n, s):
        # Compute the area
        return (0.25*n*s**2)/(math.tan(math.pi/n))

    def perimeter(n, s):
        # Compute the square of its perimeter
        return (n*s)**2

    sum = area(n, s) + perimeter(n, s)
    return round(sum, 4)
