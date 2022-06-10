import requests
from requests import Response
from lxml import etree

url = 'https://www.mzitu.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}


def download(url: str) -> str:
    resp: Response = requests.get(url, headers=headers,verify=False)
    if resp.status_code == 200:
        return resp.text


if __name__ == "__main__":
    text: str = download(url)

    root = etree.HTML(text)  # element 的元素对象
    https = root.xpath('//div[@class="postlist"]//img[@class="lazy"]/@data-original')
    print(https)
