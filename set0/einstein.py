def einstein(m):
    c = 300000000
    return f'E: {m * c**2}'

def main():
    mass = int(input('m: '))
    print(einstein(mass))

if __name__ == "__main__":
    main()

