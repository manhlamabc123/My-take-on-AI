#Data types
#Int
from unicodedata import name


-1234
345

#Float
1234.0
-465.8

#String
'4.6'
"hello123"

#Bool
True 
False

#Output and Printing
print('Hello World!', '4.5', 4.5, False, end='\n')
print('Hello World!', '4.5', 4.5)

#Variables
hello = 'tim'
world = 'world'
worldClass = hello
hello_1 = 'no'
print(hello_1, worldClass)

#Input
# name = input('Name: ') #default return string
# print(name)

#Arithmetic Operators
x = 10
y = 3
result0 = x + y
result1 = x - y
result2 = x * y
result3 = x / y
result4 = x // y #give int result, remove all decimal point
result5 = x % y #mod
print(result0, result1, result2, result3, result4, result5)

# num = input('Number: ')
# print(float(num) - 5) # one float var, return float

#String Methods
hello = 'hello'.upper() #How to use a method
print(type(hello)) #How to check var's type
print(hello)
print(hello.lower())
print(hello.capitalize())
print(hello.capitalize().count('L'))
x = 'hello'
y = 3
print(x * y) #Multiple string
print(x + str(y)) #Add 2 strings

#Conditional Operators
# ==, !=, >=, <= ,> ,<
print(ord('Z')) #print Asci code of letter
print('ab' > 'b')

#Chain Conditional
z = 3
x = 3
result = z - 2 < x + 2
# and, or, not
print(not result and not x > 6)

# If, else if, else
# x = input('Name: ')
if x == 'Manh':
    print('Hello', x)
elif x == 'Cam':
    print('Hello orange')
else:
    print('Hello whoever you are.')

#Collection
#List
x = [4, True, 'hi'] #Order matter, and maintain
x.append('hello') #add element
x.extend([4, 5, 6]) #add a list to a list
x.pop() #pop the last element
x.pop(3) #pop by index, count from 000 
print(len(x))
print(x)
print(x[2]) #Access by index

## Lists are Mutable, means: x stores reference to the list, no the copy of it
y = x
x[0] = 'hello'
print(x, y)
y = x[:] # How to copy a lists

#Tuples
x = (0, 0, 2, 2) #Tuples are Immutable, can NOT append, remove, change elements
#List can contain List and Tuples, same with Tuples

#Loops
## for
for i in range(10): #range(start, stop, step), default range(0, stop, 1)
    print(i, end = ' ')
print()
for i in [1, 2, 5, 62, 5]: #list travel
    print(i, end = ' ')
print()

x = [3,4,42,4,1,3,5,1]
### How to travel in list part 2
for i in range(len(x)):
    print(x[i], end = ' ')

### How to travel in list part 3
for i, element in enumerate(x):
    print(i, element)

## while
i = 0
while i < 10:
    print('run')
    i += 1
    if i == 5:
        print('5')
        break

# Slice Operator, use with all type of collection
x = [0,1,2,3,4,6,5,7,9,8]
y = ('hi', 'hello', 'goodbye', 'cya', 'sure')
s = 'hello'
sliced = x[:8:2] # [start:stop:step], not include [stop]
# sliced = x[::-1] # how to reverse a list
print(sliced)

#Sets - no order unique set of element. Mean: no duplicate, don't keep track of order or frequency of elements
#Use this to check if something is there or not there
#Fast to use when delete or append
x = set() #empty set
s = {4,32,3,3} #dictionary
s.add(5)
s.remove(32)
s2 = {6,1,3,5,6}
print(s)
print(32 in s)
print(s.union(s2))

#Dictionary - like Hash in other language
x = {'key': 4}
x['key2'] = 'hello' # How to add elements to Dictionary
print(x['key'])
print('key' in x)
print(list(x.values()))
print(list(x.keys()))

## How to loop through Dic
for key, value in x.items():
    print(key, value)

#Comprehensions
x = [x for x in range(5)]
x = tuple(0 for x in range(5))
x = {x % 2 for x in range(5)}
print(x)

#Functions
def func(x, y):
    print('Run')
    def func():
        print("Run run")
    func()
    return x * y, x / y

r1, r2 = func(4, 6)
print(r1, r2)

#Unpack Operator / *args and **kwargs
def func(x):
    def func2():
        print(x)
    return func2
print(func(3)())
x = func(3)
x()

x = [1,2,3,152,4,12] 
print(*x) # Unpack

def func(x, y):
    print(x, y)
pairs = [(1, 2), (3, 4)]
for pair in pairs:
    func(*pair) #*args use for list

func(**{'y': 5, 'x': 2}) #**kwargs use for dictionary
# key in this dic is the same as parameters in func

def func(*args, **kwargs):
    print(args, kwargs)

func(1,2,3,4,5, one = 0, two = 1)

# Scope & Global
x = 'tim'
def func(name):
    global x # Use this as an global var
    x = name

print(x)
func('changed')
print(x)

#Exceptions
# raise Exception('Bad')

#Handling Exceptions
try:
    x = 7 /0
except Exception as e:
    print(e)
finally:
    print('finally')

#Lambda
x = lambda x, y: x + y
print(x(2, 3))

#Map and Filter
x = [1,2,3,6,2,3,457,2,4,5,74,634,56]
map = map(lambda i: i + 2, x)
print(list(map))

map1 = filter(lambda i: i % 2 == 0, x)
print(list(map1))

# fstring
x = f'hello {6 + 8}'
print(x)