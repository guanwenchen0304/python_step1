#import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo

def replay(name):
    Userlist.insert(0,name)
    showinfo(title="GUI",message="Hello %s!"%name)
def cat():
    print ("1",end="")

def dog():
    print ("2",end="")
    

def mouse():
    print ("3",end="")
    

def elephone():
    print ("4",end="")
    

def hourse():
    print ("5",end="")
    

def fox():
    print ("6",end="")
    

def add():
    print ("7",end="")
    

def function():
    print ("8",end="")
    

def bird():
    print ("9",end="")
def change():
    print(end="\n")

interface = Tk()
interface.title("Tigergod 資工阿蓓")


#label.grid(column=0,row=0)
#button.grid(column=1,row=0)

button1 =Button(interface,text=u"1",command=(lambda: cat()))
button2 =Button(interface,text=u"2",command=(lambda: dog()))
button3 =Button(interface,text=u"3",command=(lambda: mouse()))
button4 =Button(interface,text=u"4",command=(lambda: elephone()))
button5 =Button(interface,text=u"5",command=(lambda: hourse()))
button6 =Button(interface,text=u"6",command=(lambda: fox()))
button7 =Button(interface,text=u"7",command=(lambda: add()))
button8 =Button(interface,text=u"8",command=(lambda: function()))
button9 =Button(interface,text=u"9",command=(lambda: bird()))
button10 =Button(interface,text=u"顯示",command=(lambda: change()))

#button1.grid(column=1,row=1)
button1.grid(column=1,row=1)
button2.grid(column=2,row=1)
button3.grid(column=3,row=1)
button4.grid(column=1,row=2)
button5.grid(column=2,row=2)
button6.grid(column=3,row=2)
button7.grid(column=1,row=3)
button8.grid(column=2,row=3)
button9.grid(column=3,row=3)
button10.grid(column=3,row=4)


interface.mainloop()  #进入消息循环，等待用户关闭



      

