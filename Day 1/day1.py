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