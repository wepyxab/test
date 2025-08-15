def main():
    print(fuel(input('Fraction: ')))

def fuel(s):
    while True:
        parts = s.split('/')
        if chekxy(parts):
            f = int(parts[0]) / int(parts[1])
            if f <= 0.01:
                return 'E'
            elif f >= 0.99:
                return 'F'
            else:
                return f'{round(f * 100)}%'
        else:
            s = input('Fraction: ')
            
def chekxy(s):
    try:
        x, y = int(s[0]), int(s[1])
    except ValueError: return False
    else:
        if x > y or y <= 0 or x < 0: 
            return False
        return True

if __name__ == "__main__":
    main()
