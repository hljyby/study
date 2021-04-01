import requests
import re

from requests import Response

resp: Response = requests.get("https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/03/50/224345003/224345003-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1609928499&gen=playurl&os=hwbbv&oi=1895835357&trid=16b39677816344f3bc13fc09f3021761u&platform=pc&upsig=74c9cd0531ff9c4be9b73301d44b9caf&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=298773724&orderid=2,3&agrr=1&logo=40000000")

compile = re.compile()
result = re.findall(r'<a href="(.*?)".*?>', resp.text)
