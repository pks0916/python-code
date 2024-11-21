import random

bigest_num = input('type a number: ')

if bigest_num.isdigit():
    bigest_num = int(bigest_num)

    if bigest_num <= 0:
        print('number must be bigger then 0')
        quit()
else:
    print('write a number next time')
    quit()

r = random.randint(0, bigest_num)
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess: ")

    if user_guess.isdigit():
        user_guess = int(bigest_num)

        if user_guess <= 0:
            print('number must be bigger then 0')
            quit()
    else:
        print('write a number next time')
        continue

    if user_guess == r:
        print('correct')
        break
    
    elif user_guess > r:
            print('you were above the number')
    else:
            print('u were below the number')
print("you got it in", guesses, "guesses")
    