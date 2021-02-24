import requests
# url
url = 'https://www.sogou.com/web'
kw = input('请输入关键词：')
param = {'query': kw}
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36'
}
response = requests.get(url=url, params=param, headers=headers)
page_html = response.text
fileName = kw + '.html'
with open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(page_html)
print('已完成')
