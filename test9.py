import random
ans=random.randint(0,10)
s=input("請輸入數字:")
print("你輸入的數字:",int(s))
while(ans != int(s)):
    if(ans<int(s)):
        print("你輸入的數字小於:",int(s))
    else:
        print("你輸入的數字大於:",int(s))
    print("猜吧")
    s=input("請輸入數字:")
    
        
print("答對了")

