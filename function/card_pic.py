import re


def card_address(cardcode:str):

    try:
        with open('.\\config.txt','r') as config:

            pic_address = re.search('pic_address[ \t]*=[ \t]*[^\n]+',config.read())
            if pic_address == None:
                pic_address = '.\\picture\\'
            else:
                pic_address = pic_address.group().split('=')[1].strip(' \t')
                if re.search(r'[\/\\]$',pic_address) == None:
                    pic_address = pic_address + '/'


    
    except FileNotFoundError:
        pic_address='.\\picture\\'
    
    return pic_address+cardcode+'.jpg'