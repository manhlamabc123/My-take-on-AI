def view():
    with open('passowrds.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split('|') # return a list of splitted data
            print('User:', user, '| Password:', password)

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passowrds.txt', 'a') as f:
        f.write(name + "|" + pwd + '\n')

while True:
    mode = input('Would you like to add a new password or view existing ones (view, add, quit)? ').lower()
    if mode == 'quit':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode.')
        continue