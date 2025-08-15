def main():
    while True:
        date = input('Date: ')
        try:
            print(parse_data(date))
            break
        except ValueError:
            continue

def parse_data(d):
    months = {"january": '01', "february": '02',"march": '03',"april": '04',"may": '05',"june": '06',"july": '07',"august": '08',"september": '09',"october": '10',"november": '11',"december": '12'}
    # formate mm/dd/yyyy
    if '/' in d:
        d = d.replace(' ', '').split('/')
        if len(d) != 3: raise ValueError
        month, day, year = int(d[0]), int(d[1]), int(d[2])
        if not(1 <= month <= 12 and 1 <= day <= 31 and 0 <= year):
            raise ValueError
        return f'{year:04}-{month:02}-{day:02}'
    else: # formate Month day, year
        d = d.split(' ') 
        if len(d) != 3 or ',' not in d[1]:
            raise ValueError
        get_month, day, year = d[0].lower(), int(d[1][:-1]), int(d[2])
        if get_month not in months:
            raise ValueError
        month = months[get_month]
        if not(1 <= day <= 31 and 0 <= year):
            raise ValueError
        return f'{year:04}-{month:02}-{day:02}'        
            
main()