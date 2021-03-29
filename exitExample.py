import sys

while True:
    print('Type to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.' )