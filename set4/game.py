import random
level = input('Level: ')
number = random.randint(1, int(level))
while True:
    guess = int(input('Guess: '))
    if guess < number: print('Too small!')
    elif guess > number: print('Too large!')
    else:
        print('Just right!')
        break