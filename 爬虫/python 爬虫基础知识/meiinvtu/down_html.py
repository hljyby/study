import requests
from requests import Response
from lxml import etree
from bs4 import BeautifulSoup
import os
url = 'http://www.fulimeitu.xyz/xgpic/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}


def download(url: str) -> str:
    resp: Response = requests.get(url, headers=headers, verify=False)
    if resp.status_code == 200:
        # if not os.path.exists('F:\嫩色艳图/aaa'):
        #     os.makedirs('F:\嫩色艳图/aaa')
        # with open("F:\嫩色艳图/aaa/img.jpg", "wb") as f:
        #     f.write(resp.content)
        print(1)
        return resp.text


if __name__ == "__main__":
    # text: str = download(url)
    # print(text)
    # root = etree.HTML(text)  # element 的元素对象
    # https = root.xpath(
    #     '//a[contains(@class,"next") and contains(@class,"page-numbers")]/text()')[0] == "下一页»"
    # print(https)
    # root = BeautifulSoup(text,'lxml')
    # li_list = root.select('.pagelist')[0].select('li a')
    # for i in li_list :
    #     print(i.get_text())
    #     a = i.get_text() == ">" and (int(i.get("href").split("/")[-1].split(".")[0].split("_")[-1]) <= 11)
    #     print(a)
    # a = [ "http://www.fulimeitu.xyz" + i.get("href") for i in root.select("#portfolio-grid a")]
    # a = root.select(".head h3")[0].get_text()
    # a = [ i.get("data-original") for i in root.select(".art-content a img")]
    # print(a)
    

    for i in range(10):
        download(url)