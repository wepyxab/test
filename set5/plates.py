# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


def is_valid(s):
    s = rmabc(s) # exept 0
    if 2 <= len(s) <= 6 and s[:2] == 'AA' and '2A' not in s and '0A' not in s and 'A0' not in s and (s[-1] == '2' or s[-1] == '0'):
        if ' ' not in s and '.' not in s and ',' not in s:
            return True
        else:
            return False
    else:
        return False

def rmabc(x):
    for i in 'QWERTYUIOPSDFGHJKLZXCVBNM':
        x = x.replace(i, 'A')
    for i in '13456789':
        x = x.replace(i, '2')
    return x

if __name__ == '__main__':
    main()