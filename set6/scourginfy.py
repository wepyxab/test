import sys
from csv import *

user_input = sys.argv
if len(user_input) == 3:
    if user_input[1][-4:] == '.csv' and user_input[2][-4:] == '.csv':
        try:
            with open(f'{user_input[1]}', 'r') as file:
                reader = DictReader(file)
                for row in reader:
                    surname, name = row['name'].split(',')
                    home = row['house']
                    with open(f'{user_input[2]}', 'a', newline='') as file:
                        writer = DictWriter(file, fieldnames=['name', 'surname', 'home'])
                        writer.writerow({'name': name, 'surname': surname, 'home': home})
        except FileNotFoundError as e: sys.exit(f"Could not read file {e.filename}")
    else:
        sys.exit('Not a CSV file')
elif len(user_input) < 3: print('Too few command-line arguments')
else: print('Too many command-line arguments')