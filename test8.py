import random
ans=random.randint(100,1000)
s=input("請輸入數字:")
print("你輸入的數字:",int(s))
if(int(s) != ans):
    print(int(s),"不等於",ans)
else:
    print("答對了")

