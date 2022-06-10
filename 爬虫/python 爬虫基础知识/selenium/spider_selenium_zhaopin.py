from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
import time
# chrome = Chrome(executable_path="chromedriver.exe")

options = Options()
options.add_argument("--headless") 
options.add_argument("--disable-gpu") 
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.binary_location = r'G:\新知识\爬虫\python 爬虫基础知识\chromedriver.exe' # 配置驱动器

chrome = Chrome(options=options)

chrome.get("https://www.baidu.com/")
chrome.maximize_window()
chrome.set_window_size(1920,1080)
print(chrome.get_cookies())
print(chrome.get_window_rect()) # 元素在屏幕的位置
print(chrome.get_window_size()) # 窗口的大小
chrome.find_element(By.CSS_SELECTOR,"#su")
chrome.find_element(By.CSS_SELECTOR,".title-content span.title-content-index")
time.sleep(1)
chrome.save_screenshot("a.png") # 截屏
chrome.quit()

# print(chrome.page_source)