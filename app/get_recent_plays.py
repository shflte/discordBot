import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def get_recent_plays(summoner_name):
    url = 'https://www.op.gg/summoners/tw/' + summoner_name
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')

    # 解析網頁得到你要的資訊
    title = soup.find('content-container').text

    # 將資訊轉換為JSON格式
    data = {'title': title}
    json_data = json.dumps(data)

    print(json_data)
    return

    soup_text = BeautifulSoup(html, 'html.parser').text
    json_str = json.dumps(soup_text, indent=4)
    html_dict = json.loads(json_str)

    # plays = soup.find('div', {'id': 'content-container'})
    
    # print(plays)
    # for play in plays:
    #     print(play)
    print(html_dict)
    # print(len(plays))

    # return plays
    
    # rank = soup.find('div', {'class': 'TierRank'}).text.strip()
    # win_ratio = soup.find('div', {'class': 'WinRatioTitle'}).text.strip()
    # return f'{summoner_name}的战绩：{rank}，胜率：{win_ratio}'

get_recent_plays("要邏輯有騾疾")

