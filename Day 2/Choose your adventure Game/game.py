def InvalidChoice():
    print('You have chosen the wrong path. GAME OVER!')
    quit()

def StartingState():
    choice = input("Choose your path, left or right? ").lower()
    if choice == 'left':
        RiverState()
    elif choice == 'right':
        MountainState()
    else:
        InvalidChoice()

def RiverState():
    choice = input("You are at the River, \'swim\' across or \'walk\' around? ").lower()
    if choice == 'swim':
        print('You have chosen to swim across but you were eaten by a shark. GAME OVER!')
    elif choice == 'walk':
        print('You have chosen to walk around but you have been walking for 10 days without food or drink, you dead. GAME OVER!')
    else:
        InvalidChoice()

def MountainState():
    choice = input("You are at the Mountain, there are routes A and route B, which one will you choose? A or B? ").lower()
    if choice == 'a':
        MountainRouteAState()
    elif choice == 'b':
        MountainRouteBState()
    else:
        InvalidChoice()

def MountainRouteAState():
    choice = input("You are walking on Route A, you meet a sneak? What will you do? \'Catch\' it with your Master Ball or \'beat\' it with a branch? ").lower()
    if choice == 'catch':
        print('The sneak dodged your Master Ball. You are a terrible thrower. You were attacked by the sneak. You are dead. GAME OVER!')
    elif choice == 'beat':
        print('The sneak is bigger than you. You chosen poorly. You are dead. GAME OVER!')
    else:
        InvalidChoice()

def MountainRouteBState():
    choice = input("You are walking on Route B, you meet a strange? What will you do? \'Leave\' him be or \'talk\' to him? ").lower()
    if choice == 'leave':
        print('You continued on your journey. Reached the top, saw the sun set and Win the GAME!')
    elif choice == 'talk':
        print('The man was surprised by you. He fell and took you with him. You are dead. GAME OVER!')
    else:
        InvalidChoice()

StartingState()
print('Thank you for playing!!!')