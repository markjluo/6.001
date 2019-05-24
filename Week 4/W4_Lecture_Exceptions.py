"""
Exception raised by any statement in body of try are handled by the except statement and execution continues after the body of the except statement.
"""

"""
try:
    a = int(input("a is: "))
    b = int(input("b is: "))
    print(a/b)
    print("Okay")
except:
    print("Bug in user input.")
print("Outside")
"""


# ------------------------------------------------------------------------------


try:
    a = int(input("a is: "))
    b = int(input("b is: "))
    print(a/b)
    print("Okay")
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero.")
except:
    print("Something went very wrong.")

# This is excuted when excetion of associated try body completes with no exceptions
else:
    print("No Problem")

# This is always executed after try, else and except clauses, even if they raised another error or executed
# a break, continue or return
finally:
    print("Done")


# -----------------------------------------------------------------------------------------------------------


data = []
file_name = input("Provide a name of a file of data ")

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')  # remove trailing \n (carriage return)
            data.append(addIt)
            fh.close()  # close file even if fail


# ----------------------------------------------------------------------------------------------------------------


gradesData = []
# As long as I have data (data is not empty)
if data:
    for student in data:
        try:
            name = student[0:-1]
            grades = (student[-1])
            gradesData.append([name, [grades]])

        # If the last element in the list is not a number (The person has no grade)
        except ValueError:
            gradesData.append(student[:],[])


# ---------------------------------------------------------------------------------------------------------------


test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
               [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
               [['captain', 'america'], [8.0, 10.0, 96.0]],
               [['dead', 'pool'], []]]


def avg(a):
    try:
        return sum(a)/len(a)
    except ZeroDivisionError:
        print('No test grades')
        return 0.0


def get_grades(l):
    grades = []
    for person in l:
        grades.append([person[0], person[1], round(avg(person[1]), 2)])
    return grades


print(get_grades(test_grades))


# ---------------------------------------------------------------------------------------------------------------


def fancy_divide(list_of_numbers, index):
    try:
        try:
            # Raise an exception and print out the argument '0'
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    # Print out the exception got from the try body
    except Exception as a:
        print(a)


# Since the outer try body won't execute due to zero division error
fancy_divide([0, 2, 4], 0)