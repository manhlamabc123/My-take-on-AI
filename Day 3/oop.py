from unicodedata import name


class Dog:
    def __init__(self, name): #init is a method which is called when you call the class
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def bark(self):
        print('bark')

    def add_one(self, x):
        return x + 1

d = Dog("Tim") #call the class, init is also called
d2 = Dog("Bill")
d.setName("Tim2")
d.bark()
print(d.getName(), d2.name)

print('-------------------')

#How to class is better than list or anything of kind
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def getGrade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def addStudent(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def getAvarageGrade(self):
        value = 0
        for student in self.students:
            value += student.getGrade()
        return value / len(self.students)

s1 = Student('Tim', 19, 95)
s2 = Student('Bill', 19, 75)
s3 = Student('Jill', 19, 35)

course = Course("Science", 2)
course.addStudent(s1)
course.addStudent(s2)
print(course.addStudent(s3))
print(course.getAvarageGrade())

print('-------------------')

#Inheritance
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

    def speak(self):
        print('I do not know what to say')

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')

class Dog(Pet):
    def speak(self):
        print('Bark')

class Fish(Pet):
    pass

p = Pet('Tim', 19)
p.speak()
c = Cat('Bill', 23, 'Red')
c.show()
c.speak()
d = Dog('John', 98)
d.speak()
f = Fish('Bubble', 1)
f.speak()

print('-------------------')

#Class Attribute
class Person:
    numberOfPeople = 0

    def __init__(self, name):
        self.name = name
        Person.addPerson()

    @classmethod
    def numberOfPeople_(cls):
        return cls.numberOfPeople
    
    @classmethod
    def addPerson(cls):
        cls.numberOfPeople += 1

p1 = Person('Tim')
p2 = Person('Bill')

print(Person.numberOfPeople_())

print('-------------------')

# Static Method
class Math:
    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        return 'run'

print(Math.add5(5))
print(Math.add10(5))
print(Math.pr())