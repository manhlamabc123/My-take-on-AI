import random

# random.randrange(start, stop) - does not include 10
# random.randint(start, stop) - does include 10
topRange = input('Start from: ')
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
    userNumber = int(input('Your guess (from 0 to 10 only): '))
    if userNumber == randomNumber:
        print('You guess it right!')
        print('Congratulation!!!')
        quit()
    elif userNumber < randomNumber:
        print('Higher')
    elif userNumber > randomNumber:
        print('Lower')