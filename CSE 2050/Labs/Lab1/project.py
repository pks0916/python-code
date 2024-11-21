print("wellcome to my sports quiz")

want_play = input('Would you like to play? ')

if want_play.lower() != 'yes':
    quit()

print('okay good luck, use proper grammer in the game and for number answer use an actual number for eample type 1 instead of one')
points = 0

answer = input('how many super bowls do the pats have? ')
if answer.lower() == '6':
    print('correct')
    points +=1
else:
    print('incorrect')



answer = input('who won the 2014 world cup? ')
if answer.lower() == 'germany':
    print('correct')
    points +=1
else:
    print('incorrect')


answer = input('how many teams are in the nfl? ')
if answer.lower() == '32':
    print('correct')
    points +=1
else:
    print('incorrect')


answer = input('who is the manager of the red sox? ')
if answer.lower() == 'alex cora':
    print('correct')
    points +=1
else:
    print('incorrect')



answer = input('who won the first super bowl? ')
if answer.lower() == 'packers':
    print('correct')
    points +=1
else:
    print('incorrect')

percent = (points / 5) * 100

print(f'you got', points, 'questions right')
print(f'you got', percent)