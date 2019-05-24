import random


# Create a class "Animal", which inherits from "object" class. e.g. properties of
# underlying Python object class. (Basic operations in Python, like binding variables, etc)
class Animal(object):

    creator = 'Mark'

    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    # Default argument for newname = empty string
    def set_name(self, newname=''):
        self.name = newname

    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)


class Cat(Animal):
    # Add new functionality via new methods
    def speak(self):
        print("Meow")
    # Overrides __str__ from Aminal
    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)


class Rabbit(Animal):
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        # Tag used to give unique id to each new rabbit instance
        # rid: rabbit ID
        self.rid = Rabbit.tag
        # Increase class variable "tag" every time a new instance is created
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    # Redefine '+'. e.g.: rabbit3 = rabbit1 + rabbit2
    # Equivalent to giving birth to a baby rabbit
    def __add__(self, other):
        return Rabbit(0, self, other)

    # Redefine '==' e.g.: rabbit1 == rabbit2
    # Check if the two rabbits have the same parents
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid \
                      and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent1.rid == other.parent2.rid \
                      and self.parent2.rid == other.parent1.rid
        return parents_opposite or parents_same


    def speak(self):
        print("Meep")

    def __str__(self):
        return "rabbit:" + str(self.name) + ":" + str(self.age)


class Person(Animal):

    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

    def get_fiends(self):
        return self.friends

    def add_friend(self, fname):
        self.friends.append(fname)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)

    def __str__(self):
        return "person:" +str(self.name) + ":" + str(self.age)


class Student(Person):

    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        # Will give a random number between 0 and 1
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif r < 0.5:
            print("I need sleep")
        elif r < 0.75:
            print("I should eat")
        else:
            print("I am watching TV")

    def __str__(self):
        return "student" + ":" + str(self.name) + ":" + str(self.age) + ":" + str(self.major)


jelly = Cat(1)
print(jelly.get_name())

jelly.set_name('JellyBelly')
print(jelly)

# Can still get to the underlying method
print(Rabbit.__str__(jelly))

eric = Person("eric", 45)
print(eric)

eric.speak()

a = Student("Mark", 24, "Economics")
print(a)
a.speak()

# ============================================================================

peter = Rabbit(2)
peter.set_name('Peter')
hopsy = Rabbit(3)
fupsy = Rabbit(1, peter, hopsy)
fupsy.set_name('Fupsy')
hopsy.set_name('Hopsey')
mopsy = peter + hopsy
mopsy.set_name('Mopsey')
dupsy = peter + hopsy
dupsy.set_name('Dupsy')

print(peter.rid)
print(hopsy.rid)
print(mopsy.rid)
print(dupsy.rid)
print(fupsy)

print(mopsy.get_parent1())
print(mopsy.get_parent2())
print(dupsy == mopsy)
