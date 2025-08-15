def main():
    time = convert(input('What time is it? '))
    if 7.0 <= time <= 8.0: print('breakfast time')
    elif 12.0 <= time <= 13.0: print('lunch time')
    elif 18.0 <= time <= 19.00: print('dinner time')

def convert(time):
    # 11:00 > 11.0
    time = time.split(':')
    minuts = int(time[1]) / 60
    return float(time[0]) + minuts

main()