import requests
import json
url = 'https://fanyi.baidu.com/sug'
# kw = input()
date = {'kw': 'dog'}
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36'
}
response = requests.post(url=url, data=date, headers=headers)
obj = response.json()
word = str(1)
fileName = word + '.json'
fp = open(fileName, 'w', encoding='utf-8')
json.dump(obj, fp=fp, ensure_ascii=False)
