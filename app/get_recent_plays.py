import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def get_recent_plays(summoner_name):
    url = 'https://www.op.gg/summoners/tw/' + summoner_name
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    plays_selector = '.parent-class #content-container div:nth-of-type(2) div:nth-of-type(3) li'
    plays = soup.select(plays_selector)
    for play in plays:
        print(play)
    
    # rank = soup.find('div', {'class': 'TierRank'}).text.strip()
    # win_ratio = soup.find('div', {'class': 'WinRatioTitle'}).text.strip()
    # return f'{summoner_name}的战绩：{rank}，胜率：{win_ratio}'

print(get_recent_plays("要邏輯有騾疾"))

