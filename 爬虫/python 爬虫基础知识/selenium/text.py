from selenium.webdriver import Chrome 
# from selenium.webdriver.chrome.options import Options


chrome = Chrome()

chrome.get("https://www.baidu.com/")
print(chrome.page_source)