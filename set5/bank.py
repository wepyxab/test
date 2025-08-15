def main():
    print(greet_message(input('Greeting: ')))

def greet_message(g):
    g = g.lower().lstrip()
    if g[0] == 'h' and 'hello' in g:
        return '$0'
    elif g[0] == 'h' and 'hello' not in g:
        return '$20'
    return '$100'

if __name__ == '__main__':
    main()