def main():
    print(date(input('Date: ')))

def date(s):
    while True:
        s = s.lower()
        if '/' in s: # format mm/dd/yyyy 
            s = s.replace(' ', '').split('/')
            try:
                if 1 <= int(s[0]) <= 12 and 1 <= int(s[1]) <= 31 and 0 <= int(s[2]) and len(s)==3:
                    date_values = {
                        'month': zeroday(s[0]),
                        'day': zeroday(s[1]),
                        'year': s[2]
                    }
                    return f'{date_values['year']}-{date_values['month']}-{date_values['day']}'
                else:
                    raise ValueError
            except ValueError: s = input('Date: ')
        else: #format January 1, 2001
            s = s.split(' ')
            months = {"january": '01', "february": '02',"march": '03',"april": '04',"may": '05',"june": '06',"july": '07',"august": '08',"september": '09',"october": '10',"november": '11',"december": '12'}
            try:
                if ',' in s[1] and s[0] in months and 1 <= int(s[1][:-1]) <= 31 and int(s[2]) >= 0:
                    date_values = {
                        'month': months[s[0]],
                        'day': zeroday(s[1][:-1]),
                        'year': s[2]
                    }
                    return f'{date_values['year']}-{date_values['month']}-{date_values['day']}'
                else:
                    raise ValueError 
            except (IndexError, ValueError): s = input('Date: ')

def zeroday(x):
    if len(x) == 1: return f'0{x}'
    else: return x

main()
