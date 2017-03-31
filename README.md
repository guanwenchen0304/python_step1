# python_step1
print("Hello world:") >>> Hello world:  
a=10,b=50  
print("Hello world:",a) >>> Hello world:10  
print("Hello world,a") >>> Hello world,a  
print("Hello world",a+b) >>> Hello world 60  
print("Hello world,a+b") >>> Hello world,a+b  
a+b >>> 60(加法)  
a-b >>> -40(減法)  
a*b >>> 500(乘法)  
a\b >>> 0.2(除法)  
a \ \ b >>> 0(除法取整數)  
a%b >>> 0(取餘數)  
a**b >>> 10^50(a的b次方 a^b)  
print("請填入以下基本資料表:\n") >>> 請填入以下基本資料表:(\n換行)  
a=input("名字:") >>> 名字: (鍵盤輸入名字，並把鍵盤輸入的string放至變數a裡面)  
b=input("體重:") >>> 體重: (鍵盤輸入體重，並把鍵盤輸入的string放至變數b裡面)  
c=input("身高:") >>> 身高: (鍵盤輸入身高，並把鍵盤輸入的string放至變數c裡面)  
d=input("地址:") >>> 地址: (鍵盤輸入地址，並把鍵盤輸入的string放至變數d裡面)  
print("我叫",a,"體重",b,"身高",c,"地址,d")>>>我叫冠玟體重0身高1地址2  
print("我叫,a","體重",b,"身高",c,"地址,d")>>>我叫,a體重0身高1地址,d  
print("y = 100*(a^2)+2b",100*(a**2)+2*b )  
a=100</br>
if(a>100):</br>
print("a大於100")</br> 
else:</br>
print("a小於100")</br>
s = input("請輸入數字:")</br>
print("請輸入數字:",int(s))</br>
if(int(s)>100):</br>
print(int(s),"大於100")</br>
else:</br>
print(int(s),"小於100")  

import random 
ans=random.randint(0,10) >>> 答案在0到10間的整數
s=input("請輸入數字:") >>> 輸出 請輸入數字
print("你輸入的數字:",int(s)) >>> 指示使用者在(你輸入的數字)後打數字
while(ans != int(s)): >>> 當答案不等於使用者輸入的數字
    if(ans<int(s)): >>> 如果答案小於猜的數字
       print("你輸入的數字小於:",int(s)) >>> 打 你輸入的數字小於猜的數字:
    else: >>> 除非如果 答案大於使用者輸入的數字
       print("你輸入的數字大於:",int(s)) >>> 打 你輸入的數字大於猜的數字
    print("猜吧") >>> 顯示出請繼續猜吧
    s=input("請輸入數字:") >>> 就會輸出,請輸入數字:
print("答對了") >>> 答對了結束

a=input("請輸入a:")  
b=input("請輸入b:") 
method=input("請輸入method:")
if(int(method) == 1):
    print("a+b=",int(a)+int(b))
elif(int(method)  == 2):
    print("a-b=",int(a)-int(b))
elif(int(method) == 3):
    print("a*b=",int(a)*int(b))
else:
    print("a/b=",int(a)/int(b))
    
    def add_function(a,b):
    c = a+b
    print (c)

def decrease_function(a,b):
    c = a-b
    print (c)

def multiply_function(a,b):
    c = a*b
    print (c)

def divide_function(a,b):
    c = a/b
    print (c)
    
if __name__=="__main__":
    a=input("請輸入a:")
    b=input("請輸入b:")
    method=input("請輸入method:")
    if(int(method) == 1):
        add_function(int(a),int(b))
    elif(int(method)  == 2):
        decrease_function(int(a),int(b)) 
    elif(int(method) == 3):
        multiply_function(int(a),int(b))  
    elif(int(method) == 4):
        divide_function(int(a),int(b))
    else:
        print("錯誤")
