def main():
    print(converter(input('camelCase: ').replace(' ', '')))

def converter(name):
    snake = ''
    for n in name:
        if n == n.upper():
            snake += f'_{n.lower()}'
        else:
            snake += n
    return f'snake_case: {snake}'

main()
