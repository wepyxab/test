def convert(s):
    s = s.replace(':)', '🙂').replace(':(', '🙁')
    return s

def main():
    a = input()
    print(convert(a))

main()