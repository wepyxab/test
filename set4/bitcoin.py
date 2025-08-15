import requests
import json
import sys

def main():
    inpu = sys.argv
    try:
        if len(inpu) == 2:
            count = float(inpu[1])
        else: 
            raise IndexError
    except ValueError: sys.exit('Command-line argument is not a number')
    except IndexError: sys.exit('Missing command-line argument or too much arguments')
    else:
        print(get_price_btc(count))
        # print(f'{get_price_btc(count):.4f}')

def get_price_btc(c):
    url = 'https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin'
    responce = requests.get(url)
    data = responce.json()
    price = data['bitcoin']['usd']
    return f'${int(price) * c:,.2f}'

main()