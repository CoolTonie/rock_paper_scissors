import random

print('HELLO THERE!!!')
name=input('ENTER PLAYER NAME: \n')
print('WELCOME TO TONIES GAME OF ROCK PAPER AND SCISSORS \n', name)
print('IF YOU READY TO PLAY AGAINST THE COMPUTER', name,  'READ THE RULES AND PICK YOUR FIRST MOVE')
print('RULES OF THE GAME:\n'
        "Rock vs paper: paper wins \n"
         "Rock vs scissor: Rock wins \n"
        "paper vs scissor: scissor wins \n")

print('R.ROCK')
print('P.PAPER')
print('S.SCISSORS')

while True:
    moves= ['rock', 'paper', 'scissors']
    pcoptions= random.choice(moves)
    playerchoice= None

    while playerchoice not in moves:
        playerchoice= input('pick from rock, paper or scissors:')
    
    if playerchoice =='rock':
        print(name,':', (playerchoice))
    elif playerchoice =='paper':
        print(name,':', (playerchoice))
    elif playerchoice=='scissors':
        print(name,':', (playerchoice))

    if pcoptions =='rock':
        print('computer:',(pcoptions))
    elif pcoptions =='paper':
        print('computer:',(pcoptions))
    elif pcoptions=='scissors':
        print('computer:',(pcoptions))

    if playerchoice==pcoptions:
        print('oops!! its a tie, play again')
                
    elif playerchoice=='rock'and pcoptions=='paper':
           print('PAPER covers ROCK')
           print('PC wins!!')
           
    elif playerchoice=='paper'and pcoptions=='scissors':
           print('SCISSORS cuts PAPER')
           print('PC wins!!')
           
    elif playerchoice=='scissors'and pcoptions=='rock':
           print('ROCK HITS SCISSORS')
           print('PC wins!!')
           
    elif playerchoice=='rock'and pcoptions=='scissors':
           print('ROCK HITS SCISSORS')
           print(name, 'wins!!')
           
    elif playerchoice=='scissors'and pcoptions=='paper':
           print('SCISSORS cuts PAPER')
           print(name, 'wins!!')
           
    elif playerchoice=='paper'and pcoptions=='rock':
           print('PAPER covers ROCK')
           print(name, 'wins!!')
           
    endgame = input("Would you like to play game? Y/N: \n")
    

    if endgame=="N" or endgame =='n':
        print('THANKS FOR PLAYING TONIES ROCK PAPER SCISSORS GAME')
        break
