print('What is your name?')
name = input()
if name == 'Mary':
    print('Hello Mary')
    print()
    print('Type your password')
    password = input()
    if password == 'swordfish':
        print('Access Granted')
    else:
        print('Access Denied')
else:
    print('Imposter')