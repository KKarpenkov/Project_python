
print ('Welcome, Challanger')
print ('You have a chance to play "World of Warcraft quiz game"')

playing = input('Do you want to play? ')

score = 0

if playing.lower() == 'yes':
    print('Well, it begins')
else: 
    print ('Farawell');
    quit()
#1
answer = input ('Which company publishes "World of Warcraft"? ')
if answer.lower() == 'blizzard entertainment':
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')
    quit()
#2
answer = input ('What year was "World of Warcraft" released? ')
if answer.lower() == '2004':
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')
    quit()
#3
answer = input ('What species are most characters in the game? ')
if answer.lower() == 'humans':
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')
    quit()
#4
answer = input ('What was the first expansion added to "World of Warcraft"? ')
if answer.lower() == 'the burning crucase' or 'burning crusade':
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')
    quit()

print(f'Congratulations, you successfully completed the game, your final score is {score}!')
print(str((score // 4)*100), '%', 'of your answers was correct! ')