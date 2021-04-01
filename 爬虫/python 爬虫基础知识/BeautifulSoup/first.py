from bs4 import BeautifulSoup
from requests import Response
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}


def download(url):
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        resp.encoding = 'utf8'
        return resp.text


if __name__ == "__main__":
    url = "http://www.fulimeitu.xyz/xgpic/"
    html = download(url)
    root = BeautifulSoup(html, 'lxml')
    print(root.contents)
