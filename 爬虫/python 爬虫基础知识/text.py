import requests
from bs4 import BeautifulSoup
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Referer": "https://www.aitaotu.com/"
}

url = "https://img.aitaotu.cc:8089/Pics/2019/0221/c_114/05.jpg"

resp: requests.Response = requests.get(url, headers=headers)
if resp.status_code == 200:
    # root = BeautifulSoup(resp.text, 'lxml')
    # # a_list = root.select(".main-content .postlist #pins li>a")
    # a = root.select(".content .main-image>p>a>img")[0].get("src")
    # print(resp.content)
    with open("a.jpg",'wb') as f:
        f.write(resp.content)
    base = url[:url.rfind("/")+1] + "%s" + url[url.rfind("."):]
    # for i in range(10):
    #     # print(base % i)
    #     print(str(i).zfill(2))