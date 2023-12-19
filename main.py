import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time

from function import search,fileoutput


result = []
card = None
pack = []

def imageforTK(image:str):
    image = Image.open(image)
    image.thumbnail((200, 290))
    return ImageTk.PhotoImage(image)
#将jpg转换成tkinter可以识别的图像形式

def to_search(event=''):
        resultslist.delete(0,tk.END)
        if searchbox.get().strip(' ')!='':
            global result
            result = search.search(searchbox.get().strip(' '))
            for i in result:
                resultslist.insert(tk.END,i[1])

#调用爬虫

def display(event=''):
    if len(resultslist.curselection())==0 : return

    global card
    card = result[resultslist.curselection()[0]]
    try:
        photo = imageforTK('.\\picture\\'+card[0]+'.jpg')
    except FileNotFoundError:
         photo = imageforTK('.\\resouse\\missingcardpic.jpg')
    pic.config(image=photo)
    pic.image = photo
    
#调用卡图展示

def addcard(t=1):
    global pack
    for i in range(t):
        pack.append(card)
        packlist.insert(tk.END,card[1])

def addcard3():
    addcard(3)

#添加卡片进样板目录

def packdelete():
    if len(packlist.curselection())==0 : return
    del pack[packlist.curselection()[0]]
    packlist.delete(packlist.curselection()[0])

#删除选中卡

def packclear():
    packlist.delete(0,tk.END)
    global pack
    pack=[]

#重置样板目录

def output():
    if nameentry.get().strip(' ')!='':
        name = nameentry.get().strip(' ')
    else:
        name='ygo打印样板'+time.strftime('%m%d%H%M_%Y%m%d%H%M%S',time.localtime())
    fileoutput.newdocx(pack,name)

#调用样板生成   

##############


root = tk.Tk()
root.title('ygo简易打印样板生成')
root.geometry("850x500")
root.minsize(850,500)
#root.iconbitmap('.//resouse//L.ico')

root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure([0,1,2],weight=1)




searchblock = ttk.Frame(root,width=250)
searchblock.pack_propagate(False)
searchblock.grid(row=0,column=0,sticky='ns')

targetblock = ttk.Frame(root,width=250)
targetblock.pack_propagate(False)
targetblock.grid(row=0,column=1,sticky='ns')

configblock = ttk.Frame(root,width=250)
configblock.pack_propagate(False)
configblock.grid(row=0,column=2,sticky='ns')

################################
#初始化布局
    


searchlline = ttk.LabelFrame(searchblock,height=50,width=250,text='查找卡片')
searchlline.pack(side='top',anchor='n',fill='x')

searchbotton = ttk.Button(searchlline,width=5,text='检索')
searchbotton.pack(side='right',anchor='e',fill='both',expand=1)
searchbox = ttk.Entry(searchlline)
searchbox.pack(fill='both',expand=1)
searchbox.bind("<Return>", to_search)
searchbotton.config(command=to_search)
    
resultslist = tk.Listbox(searchblock)
resultslist.pack(anchor='center',fill='both',expand=1,padx=10,pady=10)
resultslist.bind("<<ListboxSelect>>", display)
########################    
#searchblock







yl = ttk.LabelFrame(targetblock,text='卡图')
yl.pack(anchor='center',pady=20)

photo = imageforTK('.\\resouse\\cardback.jpg')

pic = tk.Label(yl,width=200,height=290)
pic.config(image=photo)
pic.image = photo
pic.pack(anchor='center')

addlline = ttk.Frame(targetblock)
addlline.pack(pady=20)
add1 = ttk.Button(addlline,text='添加1张',command=addcard)
add3 = ttk.Button(addlline,text='添加3张',command=addcard3)
add1.pack(side='left',padx=5)
add3.pack(side='left',padx=5)

###############################
#targetblock







DocName = ttk.LabelFrame(configblock,text='文件名(留空使用默认命名)')
DocName.pack(pady=30,fill='x')
nameentry = ttk.Entry(DocName)
nameentry.pack(fill='both')

packlist = tk.Listbox(configblock,height=15)
packlist.pack(fill='x')

configline = ttk.Frame(configblock)
configline.pack()
delete = ttk.Button(configline,text='删除',command=packdelete)
clear = ttk.Button(configline,text='全部清除',command=packclear)
delete.pack(side='left',fill='x')
clear.pack(side='right',fill='x')

opbox = ttk.Frame(configblock,width=160,height=60)
opbox.pack_propagate(False)
opbox.pack(pady=10)
output = ttk.Button(opbox,text='创建样板',command=output)
output.pack(fill='both',expand=1)


###############################
#configblock




root.mainloop()
