import datetime

class Person(object):

    def __init__(self, name):
        """Create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def setBirthday(self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def getLastName(self):
        """Return self's last name"""
        return self.lastName

    # Define (Less than, 'lt'), so that person instances can be sorted.
    def __lt__(self, other):
        """Return True if self's name is lexicographically less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's name"""
        return self.name

# p1 = Person('Mark Zuckerberg')
# p1.setBirthday(5,14,84)
# p2 = Person('Drew Houston')
# p2.setBirthday(3,4,83)
# p3 = Person('Bill Gates')
# p3.setBirthday(10,28,55)
# p4 = Person('Andrew Gates')
# p5 = Person('Steve Wozniak')
#
# personList = [p1, p2, p3, p4, p5]
# personList.sort()
#
# for e in personList:
#     print(e)


class MITPerson(Person):
    nextidNum = 0  # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name)  # Initialize Person attributes
        self.idNum = MITPerson.nextidNum # MITPerson attribute: unique ID
        MITPerson.nextidNum += 1

    def getidNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name
    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)



# p1 = MITPerson('Eric')
# p2 = MITPerson('John')
# p3 = MITPerson('John')
# p4 = Person('John')
#
#
# # This gets an error.
# # Because when p1 is compared with p4, it compares their idNums using the __lt__ method of
# # MITPerson, and p4 does not have attribute idNum
# # print(p1 < p4)
#
#
# # This works however
# # Because when p4 is compared with p1, it compares their names using the __lt__ method
# # of Person. Both instances have names.
# print(p4 < p1)



# Clean up the hierarchy with class student:
# - Create a class that captures the common behaviors of subclasses
# - Think about the subclasses as a coherent whole
class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        # Return the speak method in the parent class, but add something to it
        return MITPerson.speak(self, " Dude, " + utterance)


class Grad(Student):
    pass


class Transferstu(Student):
    # Pass: null operation, do not execute
    # Continue vs Pass:
    # -Continue forces the loop to start at the next iteration while pass means "there is no code to execute here"
    #  and will continue through the remainder or the loop body.
    pass


class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, new + utterance)

    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)


def isStudent(obj):
    return isinstance(obj, Student)


# s1 = UG('Matt Damon', 2017)
# s2 = UG('Ben Affleck', 2017)
# s3 = UG('Lin Manuel Miranda', 2018)
# s4 = Grad('Leonardo di Caprio')
# s5 = TransferStudent('Robert deNiro')

# print(s1)
# print(s1.getClass())
# print(s1.speak("I need to sleep"))
# print(isStudent(s1))
# print(isinstance(s4, MITPerson))
#
# studentlist = [s1, s2, s3, s4]
#
# for person in studentlist:
#     print(person.speak('I have no idea'))
#
#
# faculty = Professor('Eric', 'Computer Science')
# print(faculty.speak('what am i doing'))
# print(faculty.lecture('what am i doing'))




class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book"""
        self.students = []  # list of Student objects
        self.grades = {}  # maps idNum-> list of grades
        self.isSorted = True  # true if self.students is sorted

    def addStudent(self, student):
        """Assumes: student is of type Student
                Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getidNum()] = []
        self.isSorted= False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
            Add grade to the list of grades for student"""
        try:
            self.grades[student.getidNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:  # return copy of student's grade. A safe practice.
            return self.grades[student.getidNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    # def allStudents(self):
    #     """Return a list of the  students in the gradebook"""
    #     if not self.isSorted:
    #         self.students.sort()
    #         self.isSorted = True
    #     # Return a copy of a sorted list of student
    #     return self.students[:]

    # Better version with generator:
    def allStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s

def gradeReport(course):
    """Assumes: course is of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is '
                + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)


ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

# Create a gradebook
six00 = Grades()

# Add students into the gradebook
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)

# Add grades into the gradebook
six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug2, 85)
six00.addGrade(ug3, 75)

print(gradeReport(six00))

# Add more grades into the gradebook
six00.addGrade(g1, 90)
six00.addGrade(g2, 45)
six00.addGrade(ug1, 80)
six00.addGrade(ug2, 75)
print()
print(gradeReport(six00))

print()
print(six00.allStudents())

students = six00.allStudents()
print(students.__next__())
print(students.__next__())
print(students.__next__())

print()

for student in students:
    print(student)