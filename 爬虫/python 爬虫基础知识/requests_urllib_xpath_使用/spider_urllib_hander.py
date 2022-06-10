import ssl
from collections import namedtuple

from urllib.request import HTTPHandler, build_opener, HTTPCookieProcessor, ProxyHandler, Request, urlopen

from urllib.parse import urlencode

from http.cookiejar import CookieJar
# cookie控制器 代理ip控制器 请求控制器
opener = build_opener(HTTPCookieProcessor(CookieJar()), HTTPHandler(), ProxyHandler(
    proxies={'http': 'http://proxy_ip:port', 'http': 'https://proxy_ip:port'}))


ssl._create_default_https_context = ssl._create_unverified_context

# request = Request(post_url,urlencode())

if __name__ == "__main__":
    abc = urlencode({"aaa": "杨博宇"}).encode("utf8")
    print(abc)
