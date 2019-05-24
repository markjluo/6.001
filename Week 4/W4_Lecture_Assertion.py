def avg(grades):
    # Raise an AssertionError if it is given an empty list of grades
    # Function ends immediately if assertion not met
    assert not len(grades) == 0, 'no grades data'
    # assert len(grades) =! 0, 'no grades data'
    print('sda')
    return sum(grades)/len(grades)



a = [1, 3, 4, 5]
b = []

avg(b)