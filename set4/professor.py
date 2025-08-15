import random

def main():
    counter = 0
    for number in get_level():
        (x, y) = number
        result = str(x + y)
        for i in range(3):
            user_answer = input(f'{x} + {y} = ')
            if user_answer == result:
                counter += 1
                break
            else: 
                print('EEE')
            if i == 2: 
                print(f'{x} + {y} = {result}')
    print(f'Score: {counter}')

def get_level():  # prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3
    while True:
        try:
            level = input('Level: ')
            return generate_integer(level)
        except ValueError: continue

def generate_integer(level):
    level = int(level)
    if not(level == 1 or level == 2 or level == 3):
        raise ValueError
    xs_and_ys = []
    for _ in range(10):
        if level == 1:
            xs_and_ys.append((random.randint(0, 9), random.randint(0, 9)))
        elif level == 2: 
            xs_and_ys.append((random.randint(10, 99), random.randint(10, 99)))
        else: 
            xs_and_ys.append((random.randint(100, 999), random.randint(100, 999))) 
    return xs_and_ys # returns list of pares x/y

main()

