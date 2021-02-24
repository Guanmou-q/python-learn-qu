import requests
url = 'https://i1.hdslb.com/bfs/face/1be72a1d15f1af5c797f1ff1ce1015cde31a9ec0.jpg@140w_140h_1c.jpg'
response = requests.get(url=url)
tou_xiang = response.content
try:

    with open('./头像.jpg', 'wb') as fp:
        fp.write(tou_xiang)
        print("保存成功")
except (Exception):
    print("保存失败")




    
