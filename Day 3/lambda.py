def func(x):
    return x + 5

func2 = lambda x: x + 5 #lambda parameter: expresion
print(func2(2))
print(func(2))

func3 = lambda x, y: x + y
print(func3(3, 4))

#Use with map() and filter()
li = [1,2,3,4,5,6,7,8,9,10]

new_list = list(map(lambda x: x + 5, li))
print(new_list)

newList = list(filter(lambda x: x%2==0, li))
print(newList)