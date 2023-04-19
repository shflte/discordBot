import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get('https://www.op.gg/summoners/tw/%E8%A6%81%E9%82%8F%E8%BC%AF%E6%9C%89%E9%A8%BE%E7%96%BE', headers=headers)

print(response.text)