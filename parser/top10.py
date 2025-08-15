import requests
from json import *
import tabulate

def main():
    print(get_top_ten())

def get_top_ten():
    coins_ids = ['bitcoin', 'ethereum', 'solana', 'ripple', 'binancecoin', 'dogecoin', 'tron', 'cardano', 'the-open-network']
    currencie = 'usd'
    url = f'https://api.coingecko.com/api/v3/simple/price?' \
        f'vs_currencies={currencie}&' \
        f'ids={','.join(coins_ids)}' \
        f'&include_market_cap=true&' \
        f'include_24hr_vol=true&' \
        f'include_24hr_change=true'
    response = requests.get(url)
    data = response.json() 
    if len(data) != len(coins_ids):
        return 'Error: not all coins get'
    else:
        return make_tablet(data)

def make_tablet(data):
    m = [['usd', 'usd_market_cap', 'usd_24h_vol', 'usd_24h_change', 'name']]
    for row in data:
        data[row]['name'] = row
        usd, usd_market_cap, usd_24h_vol, usd_24h_change, name = data[row]['usd'], data[row]['usd_market_cap'], \
            data[row]['usd_24h_vol'], data[row]['usd_24h_change'], data[row]['name']
        m.append([usd, usd_market_cap, usd_24h_vol, usd_24h_change, name])
    return m
main()