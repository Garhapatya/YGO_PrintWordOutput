# -*- coding: utf-8 -*-
import re

def getcard_address():
    try:
        with open('.\\config.txt','r',encoding='utf-8') as config:

            card_address = re.findall('^card_address[ \t]*=[ \t]*[^\n]+',config.read(),re.MULTILINE)
            
            for i in range(len(card_address)):
                card_address[i] = card_address[i].split('=')[1].strip(' \t')
                if re.search(r'[\/\\]$',card_address[i]) == None:
                    card_address[i] = card_address[i] + '/'
    except FileNotFoundError:
        card_address=[]
    
    return card_address

def getpic_address():

    try:
        with open('.\\config.txt','r',encoding='utf-8') as config:

            pic_address = re.findall('^(?:pic_address|card_address)[ \t]*=[ \t]*[^\n]+',config.read(),re.MULTILINE)
            if len(pic_address) == 0:
                pic_address.append('.\\picture\\')
            else:
                for i in range(len(pic_address)):
                    pic_address[i] = pic_address[i].split('=')[1].strip(' \t')
                    if re.search(r'[\/\\]$',pic_address[i]) == None:
                        pic_address[i] = pic_address[i] + '/'
    except FileNotFoundError:
        pic_address=['.\\picture\\']
    
    return pic_address


card_address = getcard_address()
pic_address = getpic_address()



