import collections 
from collections import Counter
from collections import namedtuple
from collections import deque

#Containers
# string
# list
# set
# dict
# tuple - immutable

# Types
# 1 counter
c = Counter('gallad')
print(c)
c = Counter(['a', 'b', 'c', 'a'])
print(c)
c = Counter(cats=4, dogs=7, birds=10)
print(c)
print(c['cats'])
print(list(c.elements()))
print(c.most_common(2)) #return 2 elements with the most amount
c = Counter(a=4, b=2, c=0, d=-2)
d = ['a', 'b', 'b', 'c']
c.subtract(d)
print(c)
c.update(d)
print(c)
c.clear()
print(c)
c = Counter(a=4, b=2, c=0, d=2)
d = Counter(['a', 'b', 'b', 'c'])
print(c + d)
print(c - d)
print(c & d) #intersection
print(c | d) #union

# 2 namedTuple()
point = namedtuple('Point', 'x y z')
point = namedtuple('Point', ['x', 'y', 'z'])
newP = point(3, 4, 5)
print(newP)
print(newP.x)
print(newP._asdict())
print(newP._fields)
newP = newP._replace(x=6) #newP._replace(x=6) only will not work because Tuple is an immutable object 
print(newP)
p2 = point._make(['a', 'b', 'c'])
print(p2)
print(p2._asdict())

# 3 deque
d = deque('Hello')
d.append(3)
print(d)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)

d.extend('3612qfa')
print(d)
d.extend('asdhflj')
print(d)
d.extendleft('MANHASDJFH')
print(d)
d.reverse()
print(d)

d.rotate() #default by rotate(1)
print(d)

d = deque('hello', maxlen=5) #maxlen cannot be change after this
d.append('e')
d.extend([1,2])
print(d)


# 4 orderDict
# 5 defaultDict