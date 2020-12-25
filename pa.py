import requests
from bs4 import BeautifulSoup

url_a = "https://www.ivsky.com/tupian/nanji_dongwu_t19645/index_"
url_b = ".html"

i: int 
for i in range(10):
    res = requests.get(url_a + str(i) + url_b)
    soup = BeautifulSoup(res.text, "html.parser")
    divs = soup.find_all("div", class_="il_img")
    list1 = []
    for div in divs:
        a = div.find_all("a")
        a = a[0]
        list1.append(a["href"])
    list2 = []
    for x in list1:
        res1 = requests.get("https://www.ivsky.com" + x)
        soup1 = BeautifulSoup(res1.text, "html.parser")
        url1 = soup1.find_all("div", id="pic_con")[0].find_all("img")[0]["src"]
        list2.append(url1)
    n = 0
    for y in list2:
        res2 = requests.get("http:" + y)
        print("正在打开第%d张图片" % (n))
        with open(str(i) + "picture" + str(n) + ".jpg", "wb+") as file:
            file.write(res2.content)
            print("已打开第%d张图片" % (n))
            n += 1
