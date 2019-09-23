#!/usr/bin/python3.6

import requests,datetime
from bs4 import BeautifulSoup

now = datetime.datetime.now()
today = now.strftime('%Y%m%d')

stock_id = input("請輸入股票代碼 : ")
url = 'https://tw.stock.yahoo.com/q/q?s='+stock_id
try:
 page = requests.get(url)
 soup = BeautifulSoup(page.content, 'html.parser')
 table = soup.find_all(text='成交')[0].parent.parent.parent
 stock_name = table.select('tr')[1].select('td')[0].text
 price = table.select('tr')[1].select('td')[2].text
 print(stock_name.strip('加到投資組合'))
 print(today,'成交價 :',price)
except:
 print('股票代碼錯誤或查無此代碼!!')