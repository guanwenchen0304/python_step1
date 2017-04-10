#import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
def replay(name):
    Userlist.insert(0,name)
    showinfo(title="GUI",message="Hello %s!"%name)

def add_function(a,b):
    c = a+b
    print (c)
    showinfo(title="GUI",message="%d!"%c)
    Userlist.insert(0,c)
def decrease_function(a,b):
    c = a-b
    print (c)
    showinfo(title="GUI",message="%d!"%c)
    Userlist.insert(0,c)


interface = Tk()
interface.title("Tigergod 資工阿蓓")
label=Label(interface, text="Hello!")   #建立標籤物件
label.pack()       #顯示元件
button=Button(interface,text="OK")
button.pack()     #顯示元件

#label.grid(column=0,row=0)
#button.grid(column=1,row=0)
a=int(input("a:"))
b=int(input("b:"))
Userlist =Listbox(interface)
button1 =Button(interface,text=u"加法",command=(lambda: add_function(a,b)))
button2 =Button(interface,text=u"減法",command=(lambda: decrease_function(a,b)))
ent=Entry(interface)
 
ent.pack()
#button1.grid(column=1,row=1)
button1.pack()
button2.pack()



Userlist.pack()  #放到主体窗口
interface.mainloop()  #进入消息循环，等待用户关闭



      

