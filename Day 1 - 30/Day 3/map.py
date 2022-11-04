li = [1,2,3,4,5,6,7,8,9,10] # do not name a list as 'list'

def func(x):
    return x**x

map = map(func, li) #map(function, list)
print(list(map))
print([func(x) for x in li if x % 2 == 0])