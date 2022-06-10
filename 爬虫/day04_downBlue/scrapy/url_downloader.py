from urllib3.poolmanager import PoolManager
from urllib3 import HTTPResponse


# print(res.status)


def down_html(url, enconding="UTF-8", method="get"):
    http = PoolManager()
    res: HTTPResponse = http.request(method=method, url=url, headers={# enconding=enconding
        # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"})
        "user-agent": "Mozilla / 5.0(iPhone CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38(KHTML,like Gecko) Version/11.0 Mobile/15 A372 Safari/604.1"})
    if res.status == 200:
        return res.data.decode()
    else:
        return False


if __name__ == "__main__":
    print(down_html("https://w13.wme6aqx1.club/2048/thread.php?fid-15.html"))
