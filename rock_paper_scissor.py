'''[Rock Paper Scissors]
This is a simple two-player game where, at a signal,
players make figures with their hands, representing 
a rock, a piece of paper , or a pair of scissors,
The winner is determined according to a set of rules


RULE:

1.    Rock beats scissors, scissors beat paper, and paper beats rock.
2.    Agree ahead of time whether you will count off “rock, paper, scissors, shoot” or just “rock, paper, scissors.”
3.    Use rock, paper, scissors to settle minor decisions or simply play to pass the time.

4. if two players input same thing, it's a Tie -- replay
'''

#study the game rule

import random as rd

print("Welcome to ROCK PAPER SCISSOR\n")

options = ('r','p','s')


print('1 - Play\n0 -  To Exit')
player_option = input('Enter an Option: ')

while player_option == '1':
    print('Here are the available Options:\n')
    print('R - Rock\nP - Paper\nS - Scissor\n')

    print('**************** Player **********************')
    p1_name = 'You'
    p1_select = input('Enter Your Selection: ').lower()
    

    if p1_select == 'r' or p1_select == 'p' or p1_select == 's':

        print('**************** Player Two *******************')
        p2_name = 'The Computer'
        p2_select = options[rd.randint(0, 2)].lower()
        print(f'The Computer Selected {p2_select}')
        

        if(p2_select == 'r' or p2_select == 'p' or p2_select == 's'):
            
            #check winner

            if(p1_select == 'r' and p2_select == 's'):
                winner = p1_name

            elif(p1_select == 's' and p2_select == 'p'):
                winner = p1_name

            elif(p1_select == 'p' and p2_select == 'r'):
                winner = p1_name

                #for p2_select
            elif(p2_select == 'r' and p1_select == 's'):
                winner = p2_name

            elif(p2_select == 's' and p1_select == 'p'):
                winner = p2_name

            elif(p2_select == 'p' and p1_select == 'r'):
                winner = p2_name
            else:
                winner = 'Tie'
            #check winner end
            
            print('**************************************************')
            if(winner == 'Tie'):
                print("It's a TIE will be replayed")
                print('**************************************************')
            else:
                print(f'{winner} Won')
                

            #print replay option
            print('1 - Replay\n0 -  To Exit')
            player_option = input('Enter an Option: ')

            
        else:
            print('***************** Wrong Input *****************\n')
        
    else:
        print('***************** Wrong Input *****************\n')
        
print('****************** Game Over ********************')
        
    
        

    

