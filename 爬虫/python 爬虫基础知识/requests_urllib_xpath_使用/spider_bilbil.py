import requests
import re

import ssl

from requests import Response
ssl._create_default_https_context = ssl._create_unverified_context

header = {
    # "authority": "upos-sz-mirrorcos.bilivideo.com",
    # "method": "GET",
    # "path": "/upgcxcode/03/50/224345003/224345003-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1609928499&gen=playurl&os=cosbbv&oi=1895835357&trid=16b39677816344f3bc13fc09f3021761u&platform=pc&upsig=7a7d3b4349ebf6c9baa54550779d251f&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=298773724&orderid=2,3&agrr=1&logo=40000000",
    # "scheme": "https",
    # "if-range": "19b701b3a125738f8a3a4dda055e759a",
    "origin": "https://www.bilibili.com",
    "referer": "https://www.bilibili.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

resp: Response = requests.get("https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/03/50/224345003/224345003-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1609928499&gen=playurl&os=hwbbv&oi=1895835357&trid=16b39677816344f3bc13fc09f3021761u&platform=pc&upsig=74c9cd0531ff9c4be9b73301d44b9caf&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=298773724&orderid=2,3&agrr=1&logo=40000000", headers=header)

# compile = re.compile()
# result = re.findall(r'<a href="(.*?)".*?>', resp.text)
with open("b.mp4","wb") as f:
    f.write(resp.content)