import random, sys
print('ROCK, PAPER, SCISSORS')
#initialize variables
wins = 0
losses = 0 
ties = 0

while True:#game main loop 
    print('%s Wins, %s Losses, %s Ties'%(wins, losses, ties))
    while True:#player input loop
        print('Enter your move: (r)ock (p)aper (s)cissor or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #exit the game
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s or q')
        
    #display the player move
    if playerMove == 'r':
        print('ROCK versus....')
    elif playerMove == 'p':
        print('PAPER versus....')
    elif playerMove == 's':
        print('SCISSOR versus....')
        
    #display the computer move
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSOR')
        
    #display and recodrd the win/loss/tie
    if playerMove == computerMove:
        print('It\'s a tie!')
        ties =+ 1
    if playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins =+ 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins =+ 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins =+ 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You loose!')
        losses =+ 1
    elif playerMove == 'p' and computerMove == 's':
        print('You loose!')
        losses =+ 1
    elif playerMove == 's' and computerMove == 'r':
        print('You loose!')
        losses =+ 1
        
            