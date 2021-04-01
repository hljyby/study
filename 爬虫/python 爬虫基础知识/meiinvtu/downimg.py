import os

from requests import Response
import requests


def downloadImg(url, headers):
    resp: Response = requests.get(url, headers=headers,proxies={
        "http":'http://110.243.5.230:9999'
    })
    if resp.status_code == 200:
        return resp.content
    print("下载失败")
    print(resp.text)

if __name__ == "__main__":
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Referer": "https://www.mzitu.com/"
    }
    base_dir = os.path.abspath(".")
    dir_name = os.path.join(base_dir, "meiinvtu")
    print(base_dir)
    print(dir_name)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    for i in range(1, 200):
        ii = str(i).zfill(2)
        print(ii)
        url = f"https://imgpc.iimzt.com/2020/03/09a{ii}.jpg"
        # headers.update({"referer": f"https://www.mzitu.com/224549/{i}"})
        img_name = url.split("/")[-1]
        all_name = os.path.join(dir_name, img_name)
        if os.path.exists(all_name):
            continue
        content = downloadImg(url, headers)
        print(img_name)
        print(all_name)
        if content:
            with open(all_name, 'wb') as f:
                f.write(content)
        else:
            break


# https://img.souutu.com/2020/1229/20201229102452636.jpg.1680.0.jpg
# https://img.souutu.com/2020/1229/20201229102452566.jpg.1680.0.jpg
# https://img.souutu.com/2020/1229/20201229102452846.jpg.1680.0.jpg
# https://img.souutu.com/2020/1229/20201229102453228.jpg.1680.0.jpg
# https://img.souutu.com/2020/1229/20201229102453415.jpg.1680.0.jpg
# https://img.souutu.com/2020/1229/20201229102453139.jpg.1680.0.jpg
# https://img.souutu.com/2020/1229/20201229102453816.jpg.1680.0.jpg
# https://img.souutu.com/2020/1229/20201229102454153.jpg.1680.0.jpg

# 20200914084221836.jpg

# 20201130091509302.jpg.

# 20200702015713541.jpg

# https://img.souutu.com/2020/1123/20201123011745527.gif