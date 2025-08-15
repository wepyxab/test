import sys
import tabulate
from csv import *

user_input = sys.argv
if len(user_input) == 2:
    if user_input[1][-4:] == '.csv':
        try:
            with open(f'{user_input[1]}') as file:
                data = []
                reader = DictReader(file)
                for row in reader:
                    data.append(row)
                    print(data)
                print(tabulate.tabulate(data, headers='keys', tablefmt='grid'))

        except FileNotFoundError: sys.exit()
    else:
        sys.exit('Not a CSV file')
elif len(user_input) < 2: print('Too few command-line arguments')
else: print('Too many command-line arguments')