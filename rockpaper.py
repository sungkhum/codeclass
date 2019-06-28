#
# Your name: Nathan Wells
#
# Date: Tue., June 18, 2019
#
# Here is a short python program... try it out!
# 
# Comments are in red.


import time          # includes a library named time
import random        # a random library

i = 0
name = input('Hi... what is your name? ')   
print

if name == 'Matt' or name == 'Colleen':
    print('I\'m "offline." Try later.')

elif name == 'Matthew':                            
    print('Matthew Jeffryes!?!')
    time.sleep(.5)             
    print('No?')
    time.sleep(.5)
    print('Meh.')

else:                   
    print('Welcome,', name)
    while i < 2:
        if i == 0:
            print('Let\'s play rock, paper, scissors!')
            i = 1
        else:
            print('========================================')
            print('Let\'s play rock, paper, scissors again!')
            print('========================================')
        user_choice = input('Type rock, paper or scissors: ') 
        if user_choice == 'rock':
            my_choice = 'paper'
            print('I chose:', my_choice)
            print('You LOOSE! I WIN!')
        elif user_choice == 'paper':
            my_choice = 'scissors'
            print('I chose:', my_choice)
            print('You LOOSE! I WIN!')
            if i > 0:
                print('You\'re not very good at this are you...')
        elif user_choice == 'scissors':
            my_choice = 'rock'
            print('I chose:', my_choice)
            if i > 0:
                print('You loose again! I WIN!')
            else:
                print('You LOOSE! I WIN!')
        elif user_choice == 'quit' or user_choice == 'exit':
            print('==================================')
            print('Fine looser - I\'ll beat you later')
            print('==================================')
            i = 5
        else:
            print("That's not a valid play. Check your spelling!")
    



# The lab problem (problem 1) is to run + submit this file, hw0pr1.py
#
#   Submit it at     www.cs.hmc.edu/submit
#   Login with passwd "asdf" (which you should then change)
#
# Gold/black have different problems for #2... (check the site)
#

