# !/usr/bin/env python
# -*- coding: utf-8 -*-# 
# @Author  : Ailie
# @File    : mailLogin.py
# @Software: PyCharm
import time
import unittest 
from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as EC
class mailLogin(unittest.TestCase):
    def setUp(self):
        url = 'https://mail.yeah.net/'
        self.browser = webdriver.Chrome()
        self.browser.get(url)
        time.sleep(5)    
    def test_login_01(self):
        '''
        用户名、密码为空
        '''
        self.browser.switch_to.frame("x-URS-iframe")
        self.browser.find_element_by_name('email').send_keys('')
        self.browser.find_element_by_name('password').send_keys('')
        self.browser.find_element_by_id('dologin').click()
        self.browser.switch_to.default_content()
        time.sleep(3)
        name = self.browser.find_element_by_id('spnUid')        
        if name == 'sanzang520@yeah.net':
            print('登录成功')        
        else:
            print('登陆失败')    
    def test_login_02(self):
        '''
        用户名正确、密码为错误
        '''
        self.browser.switch_to.frame("x-URS-iframe")
        self.browser.find_element_by_name('email').send_keys('sanzang520')
        self.browser.find_element_by_name('password').send_keys('xxx')
        self.browser.find_element_by_id('dologin').click()
        self.browser.switch_to.default_content()
        time.sleep(3)
        name = self.browser.find_element_by_id('spnUid')        
        if name == 'sanzang520@yeah.net':
            print('登录成功')        
        else:
            print('登陆失败')    
    def test_login_03(self):
        '''
        用户名、密码正确
        '''
        self.browser.switch_to.frame("x-URS-iframe")
        self.browser.find_element_by_name('email').send_keys('sanzang520')
        self.browser.find_element_by_name('password').send_keys('xxx')
        self.browser.find_element_by_id('dologin').click()
        self.browser.switch_to.default_content()
        time.sleep(3)
        name = self.browser.find_element_by_id('spnUid')        
        if name == 'sanzang520@yeah.net':
            print('登录成功')        
        else:
            print('登陆失败')    
    def tearDown(self):
        self.browser.quit()
if __name__ == "__main__":
    unittest.main()