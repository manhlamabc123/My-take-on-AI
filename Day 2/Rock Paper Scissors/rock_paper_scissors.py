import random

userWins = 0
compWins = 0

def compChoiceGenarator():
    compChoice = random.randint(1, 3)
    if compChoice == 1:
        compChoice = 'R'
    elif compChoice == 2:
        compChoice = 'P'
    else:
        compChoice = 'S'
    return compChoice

def userChoiceInput():
    userChoice = input('Your choice (R/P/S or quit): ').upper()
    if userChoice not in ['R', 'P', 'S', 'QUIT']:
        print('Please only choose R/P/S or quit.')
        return
    return userChoice

def RPSResult(userChoice, compChoice):
    if userChoice == 'R':
        if compChoice == 'R': return 'Draw'
        elif compChoice == 'P': return 'User Lose'
        else: return 'User Win'
    if userChoice == 'P':
        if compChoice == 'P': return 'Draw'
        elif compChoice == 'S': return 'User Lose'
        else: return 'User Win'
    if userChoice == 'S':
        if compChoice == 'S': return 'Draw'
        elif compChoice == 'R': return 'User Lose'
        else: return 'User Win'

while True:
    userChoice = userChoiceInput()
    if userChoice == 'QUIT':
        break
    elif userChoice == None:
        continue 
    else:
        compChoice = compChoiceGenarator()
        result = RPSResult(userChoice, compChoice)
        if result == 'User Win':
            print('User win.')
            userWins += 1
        elif result == 'User Lose':
            print('User lose.')
            compWins += 1
        else: print('A Draw')
        print('User: ', userWins, ' - Computer: ', compWins)