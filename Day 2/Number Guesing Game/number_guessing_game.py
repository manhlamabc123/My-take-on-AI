import random

# random.randrange(start, stop) - does not include 10
# random.randint(start, stop) - does include 10
guessTime = 0

topRange = input('From 0 to ? ')
if topRange.isdigit():
    topRange = int(topRange)
    if topRange <= 0:
        print('Please type a number greater than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()
randomNumber = random.randint(0, topRange)

while True:
    guessTime += 1
    userNumber = input('Your guess: ')
    if userNumber.isdigit():
        userNumber = int(userNumber)
        if userNumber < 0 or userNumber > topRange:
            print('This number is not even in the range.')
    if userNumber == randomNumber:
        print('You guess it right!')
        print('Congratulation!!!')
        break
    elif userNumber < randomNumber:
        print('Higher!')
    elif userNumber > randomNumber:
        print('Lower!')

print(f'It took you {guessTime} to find the number.')