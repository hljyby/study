from urllib3.poolmanager import PoolManager
from urllib3 import HTTPResponse


# print(res.status)


def down_html(url, enconding="UTF-8", method="get"):
    http = PoolManager()
    res: HTTPResponse = http.request(method=method, url=url, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"})
    if res.status == 200:
        return res.data.decode()
    # enconding=enconding
    else:
        return None


if __name__ == "__main__":
    print(down_html("https://wp.m.163.com/163/page/news/virus_report/index.html"))
