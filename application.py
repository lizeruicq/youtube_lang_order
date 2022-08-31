import re
import time,os
from selenium import webdriver
from bs4 import BeautifulSoup

lang = ['中文','英语','中文（繁体）','德语','法语','韩语','越南语','印度尼西亚语','泰语','西班牙语','葡萄牙语','俄语']

base_url = 'https://studio.youtube.com/video/b2DNOZRCFPY/translations'

option = webdriver.ChromeOptions()
option.add_argument(r'user-data-dir=C:\Users\zerui.li\AppData\Local\Google\Chrome\User Data')

driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe", options= option)

driver.get(base_url)
driver.implicitly_wait(10)

driver.find_element_by_id('add-translations-button').click()
time.sleep(2)
pageSource = driver.page_source
soup = BeautifulSoup(pageSource,'html.parser')

pat = re.compile(r'(.*)id="text-item-(.*)"(.*)')

def template(a,b):
    print('//'+ a +'\nvar button = document.getElementById('+ b +')'+'\nbutton.click()')


temp = {}
for item in soup.find_all('yt-formatted-string'):
    if item.text in lang:
        # print(item.text)
        parent = item.find_parent('tp-yt-paper-item')
        parent = str(parent)
        #id="text-item-1"
        a = re.match(pat,parent)
        a = a.group().split(' ')[6]
        temp[item.text] = a

for i in temp:
     template(i,temp[i])






