print("壽司店菜單:\n")

print("a=50")
print("b=40")
print("c=55")
print("d=60")
a=50
b=40
c=55
d=60
W1=0
W2=0
W3=0
W4=0

keep = input("請問要點餐嗎(y/n)")
while(keep == 'y'):
    O=input("請問你要什麼")
    if(O == 'a'):
        W1=int(input("請問a要幾個"))
        a=50
        print("金額=",(a*W1))
    if(O == 'b'):
        W2=int(input("請問b要幾個"))
        b=40
        print("金額=",(b*W2))
    if(O == 'c'):
        W3=int(input("請問c要幾個"))
        c=55
        print("金額=",(c*W3))
    if(O == 'd'):
        W4=int(input("請問d要幾個"))
        d=60
    keep = input("請問要繼續點餐嗎(y/n)")
print("總金額",(a*W1)+(b*W2)+(c*W3)+(d*W4))



    

