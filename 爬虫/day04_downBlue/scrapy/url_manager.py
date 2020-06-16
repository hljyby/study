# url管理器，通过两个set来完成url的管理

class UrlManager():
    # 创建set集合
    def __init__(self):
        self.new_url = set()
        self.old_url = set()

    # 编写一个方法，添加url
    def add_url(self, url):
        if (url not in self.new_url) and (url not in self.old_url):
            self.new_url.add(url)

    # 编写一个方法可以同时添加多个url
    def add_urls(self, urls):
        for url in urls:
            self.add_url(url)

    # 随即返回一个带下载的url地址
    def get_url(self):
        # 随机返回
        url = self.new_url.pop()
        # 添加到已下载的set合集中
        self.old_url.add(url)
        return url

    # 编辑一个方法，是否存在待下载的url
    def has_url(self):
        return len(self.new_url) > 0


# 单元测试代码在模块被调用时不会触发

if __name__ == "__main__":
    um = UrlManager()
    um.add_urls(["http://www.163.com", "http://www.163.com", "http://www.baidu.com"])
    print (um.get_url())