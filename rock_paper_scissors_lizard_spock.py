import random 

user_wins = 0 
comp_wins = 0 
options = ['rock', 'paper', 'scissors', 'lizard', 'spock']

while True:
    user_input = input('Type: Rock/Paper/Scissors/Lizard/Spock or press Q to quit ').lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,4) 
    comp_pick = options[random_number]
    print('Computer picked', comp_pick + '.')

    if user_input == 'rock' and comp_pick == 'scissors': 
        print('You won!')
        user_wins += 1
        continue
    elif user_input == 'rock' and comp_pick == 'lizard':
        print('You won!')
        user_wins += 1
        continue
    
    elif user_input == 'paper' and comp_pick == 'rock' :
        print('You won!')
        user_wins += 1
        continue
    elif user_input == 'paper' and comp_pick == 'spock':
        print('You won!')
        user_wins += 1
        continue
 
    elif user_input == 'scissors' and comp_pick == 'paper': 
        print('You won!')
        user_wins += 1
        continue
    elif user_input == 'scissors' and comp_pick == 'lizard':
        print('You won!')
        user_wins += 1
        continue
    
    elif user_input == comp_pick:
        print('It is draw, try again!')
        continue
    
    elif user_input == 'lizard' and comp_pick == 'paper':
        print('You won!')
        user_wins += 1
        continue
    elif user_input == 'lizard' and comp_pick =='spock':
        print('You won!')
        user_wins += 1
        continue
    elif user_input == 'spock' and comp_pick == 'scissors':
        print('You won!')
        user_wins += 1
        continue
    elif user_input == 'spock' and comp_pick == 'rock':
        print('You won!')
        user_wins += 1
        continue
    else: 
        print('You lost')
        comp_wins += 1
        continue
print('You won', user_wins, 'times')
print('The computer won', comp_wins, 'times')
print('Goodbye!')
