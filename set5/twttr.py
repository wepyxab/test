

def main():
    print(shorten(input('Word: ')))

def shorten(word):
    c = ''
    for i in word:
        if i not in 'AEIOUaeiou':
            c += i
    return c
    
if __name__ == "__main__":
    main()