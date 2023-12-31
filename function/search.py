# -*- coding: utf-8 -*-
from urllib import parse
import requests
from bs4 import BeautifulSoup

import re
import os

from function.getconfig import card_address


def websearch(name:str,page = 1) -> list:
    url = 'https://www.ourocg.cn/search/'+parse.quote(name)+'/'
    if page!=1 : url = url + str(page)
    

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    #用bs储存html文本方便后续处理

    store = soup.find_all('script',text = re.compile('window.__STORE__ = .*'))
    cards_info = re.findall('"password":"[0-9]+","name":"[^"]+"',store[0].contents[0])
    #ourocg会用一个包在<script>里的'window.__STORE__ ='来储存本页所有卡片的效果和其他信息，在这里用两次正则检索出来每张卡片的卡密和卡名
    
    #print(cards_info)

    if len(cards_info)==0 :
        return []
        #递归终点，如果正则没检索到东西就代表没有下一页了

    Cards = []
    for i in cards_info:
        info = i.split(',')
        card_code = info[0].split(':')[1].strip('"').lstrip('0')
        card_name = info[1].split(':')[1].strip('"')
        Cards.append((card_code,card_name))
        #用split和strip进行卡密卡名格式整理，从原来的字符串输出成元组方便处理数据

    Cards.extend(websearch(name,page+1))
    #递归来遍历所有页数

    #print(tuples)
    return Cards


def localsearch(name:str) ->list:
    Cards = []

    for i in card_address:
        for root,dirs,files in os.walk(i):
            for file in files:
                if re.search(name+'[.]{0,3}[^$]',file):
                    Cards.append((os.path.splitext(file)[0],os.path.splitext(file)[0]))

    return Cards




def search(name:str) ->list:
    Cards = localsearch(name)
    #从本地搜索字典
    Cards.extend(websearch(name))
    #从网络搜索字典
    
    return Cards