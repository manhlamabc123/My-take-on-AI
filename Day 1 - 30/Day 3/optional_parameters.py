def func(x=1): #how to put in default value
    return x **2 #power of 2

call = func()
print(call)

def func(word, add = 1, freq = 2):
    print(word * (freq + add))

call = func('manh')

# How to use it with Class
class Car(object):
    def __init__(self, make, model, year, condition = 'New', kms = 0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms
    
    def display(self, showAll = True):
        if showAll:
            print('This car is a %s %s form %s, it is %s and has %s kms.' %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print('This car is a %s %s from %s.' %(self.make, self.model, self.year))

whip = Car('Ford', 'Fusion', 2021)
whip.display()
whip.display(False)

whip = Car('Ford', 'Fusion', 2021, 'Old', 12)
whip.display()
whip.display(False)