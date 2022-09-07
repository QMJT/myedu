# -*- coding:utf-8 -*-
# @Time    : 2022/9/7 19:13
# @FileName: chromediver.py
# @Software: PyCharm
# -*- coding:utf-8 -*-
# @Time    : 2022/9/4 12:55
# @FileName: charmdriver.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from time import sleep

# driver = webdriver.Chrome()  # 打开浏览器
#
# driver.get('https://www.baidu.com')  # 访问网址
# # //*[@id="kw"]
#
# element = driver.find_element(By.ID, 'kw')
#
# element.send_keys('xiakexing')  # 输入框输入文本，
# driver.find_element(By.ID, 'su').click()
#
# # find_element_class_name
#
# sleep(3)
# driver.quit()

with webdriver.Chrome() as driver:
    driver.get('https://www.baidu.com')
    element = driver.find_element(By.ID, 'kw')
    element.send_keys('xiakexing')
    driver.find_element(By.ID,'su').click()
    sleep(3)
