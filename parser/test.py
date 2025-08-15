import requests

def get_top_ten():
    # Список ID монет (можно добавить больше)
    coin_ids = ['bitcoin', 'ethereum', 'xrp', 'binancecoin', 'cardano', 
                'solana', 'dogecoin', 'polkadot', 'shiba-inu', 'tron']
    
    # Формируем URL без лишних параметров
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coin_ids)}" \
          f"&vs_currencies=usd" \
          f"&include_market_cap=true" \
          f"&include_24hr_vol=true" \
          f"&include_24hr_change=true"
    
    response = requests.get(url)
    data = response.json()
    print(data)

get_top_ten()