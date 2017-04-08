#import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
def replay(name):
    Userlist.insert(0,name)
    showinfo(title="GUI",message="Hello %s!"%name)
    
interface = Tk()
interface.title("Tigergod 資工阿蓓")
label=Label(interface, text="Hello!")   #建立標籤物件
label.pack()       #顯示元件
button=Button(interface,text="OK")
button.pack()     #顯示元件

#label.grid(column=0,row=0)
#button.grid(column=1,row=0)

button1 =Button(interface,text=u"顯示",command=(lambda: replay(ent.get())))
ent=Entry(interface)
 
ent.pack()
#button1.grid(column=1,row=1)
button1.pack()

Userlist =Listbox(interface)

Userlist.pack()  #放到主体窗口
interface.mainloop()  #进入消息循环，等待用户关闭



      

