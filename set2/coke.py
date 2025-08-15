count = 0
while count < 50:
    print(f'Amount Due: {50 - count}')
    count += int(input('Insert Coin: '))

print(f'Change Owed: {count - 50}')