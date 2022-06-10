from collections import namedtuple

from urllib.request import HTTPHandler, build_opener

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
Response = namedtuple('Response', field_names=['headers', 'code', 'text', 'body', 'encoding'])
                      

def get(url):

    opener = build_opener(HTTPHandler())
    resp = opener.open(url)
    headers = dict(resp.getheaders())
    try:
        encoding = headers['Content-Type'].split("=")[-1]
    except:
        encoding = 'utf8'
    code = resp.code
    body = resp.read()
    text = body.decode(encoding)

    return Response(headers=headers, code=code, body=body, text=text, encoding=encoding)


if __name__ == "__main__":
    resp: Response = get("https://jd.com")
    
