def printmove(fr, to):
    print('Move from', str(fr), 'to', str(to))

# Move stack of discs from one tower (fr) to another tower (to):
# n = the number of towers.
# spare = the spare tower
def Towers(n, fr, to, spare):
    if n == 1:
        return printmove(fr, to)
    else:
        # Move all the discs except the largest one to the spare tower
        Towers(n-1, fr, spare, to)
        # Move the largest disc to the destination
        Towers(1, fr, to, spare)
        # Move the rest of the discs back on top of the largest one
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))