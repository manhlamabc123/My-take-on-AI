score = 0

print('-----Quiz Game----')

playing = input('Do you want to play? (Y/N): ')
if playing.lower() != 'y':
    print('See you again next time. Bye bye.')
    quit()

print('Let\'s start the game.')
print()

print('Question 1: 1 + 1 = ?')
answer1 = input('Your answer: ')
if answer1 == '2':
    print('Correct')
    score += 1
else:
    print('Incorrect')
print()

print('Question 2: 10 + 2 = ?')
answer1 = input('Your answer: ')
if answer1 == '12':
    print('Correct')
    score += 1
else:
    print('Incorrect')
print()

print('Question 3: 1 * 3 = ?')
answer1 = input('Your answer: ')
if answer1 == '3':
    print('Correct')
    score += 1
else:
    print('Incorrect')
print()

print('Question 4: 1 + 1 * 8 = ?')
answer1 = input('Your answer: ')
if answer1 == '9':
    print('Correct')
    score += 1
else:
    print('Incorrect')
print()

print('Question 5: 100 * 100 = ?')
answer1 = input('Your answer: ')
if answer1 == '10000':
    print('Correct')
    score += 1
else:
    print('Incorrect')
print()

print('Question 6: 1 + 1 + 98 = ?')
answer1 = input('Your answer: ')
if answer1 == '100':
    print('Correct')
    score += 1
else:
    print('Incorrect')
print()

print('Question 7: 0 * 46598712387654 = ?')
answer1 = input('Your answer: ')
if answer1 == '0':
    print('Correct')
    score += 1
else:
    print('Incorrect')
print()

print('Question 8: 1 - 1 = ?')
answer1 = input('Your answer: ')
if answer1 == '0':
    print('Correct')
    score += 1
else:
    print('Incorrect')
print()

print('Question 9: 1 - 100 = ?')
answer1 = input('Your answer: ')
if answer1 == '-99':
    print('Correct')
    score += 1
else:
    print('Incorrect')
print()

print('Question 10: You love math, right?')
answer1 = input('Your answer: ')
if answer1 == 'yes':
    print('Correct')
    score += 1
else:
    print('Incorrect')
print()

print(f'Your final score is {score}/10 - {int(score/10*100)}%')
if score == 10:
    print('That good. Typical Asian.')
else:
    print('Failure!!!')