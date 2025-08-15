import sys

user_input = sys.argv
if len(user_input) == 2:
    if user_input[1][-3:] == '.py':
        try:
            with open(f"{user_input[1]}", "r") as file:
                c = 0 
                for line in file:
                    line = line.lstrip()
                    if line != '' and not line.startswith('#'):
                        c += 1
                print(c)
        except FileNotFoundError: sys.exit()
    else:
        sys.exit()
elif len(user_input) < 2: print('Too few command-line arguments')
else: print('Too many command-line arguments')