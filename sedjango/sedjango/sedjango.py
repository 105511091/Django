# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 13:19:06 2022

@author: User
"""

import requests
from bs4 import BeautifulSoup

import db

from datetime import datetime as dt # 抓日期函式庫

today = dt.today() # 抓今天的日期格式

todayS = today.strftime('%Y') # 將設定好的日期格式轉換為字串使用


url = "https://kariyushi-aquarium.com/tc/animals/lists/?animals_category=types&"

payload = {'id':'34'}

data = requests.get(url,params=payload).text

soup = BeautifulSoup(data,'html.parser')

goods=soup.find('ul',class_='lists')

allgoods=goods.find_all('li')


cursor = db.conn.cursor()


for row in allgoods:
     link = row.find('a').get('href')
     link="kariyushi-aquarium.com"+link
     price = 0
     photo = row.find('img').get('src')    
     
     title = row.find('b').text
     
    
    
     print(link)
     print(photo)
     print(title)
     print()
    

     sql = "select * from animals where name='{}' ".format(title)
    
     cursor.execute(sql)
     db.conn.commit()
    
     if cursor.rowcount == 0 :  # 表示沒有該產品
         sql = "insert into goods(name,price,goods_url,photo_url,create_date,discount) values('{}','{}','{}','{}','{}','0')".format(title,price,link,photo,todayS)
         cursor.execute(sql)
         db.conn.commit()
        
    
db.conn.close()