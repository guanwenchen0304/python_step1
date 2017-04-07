print("體育館借用球單:\n")

print("a=籃球")
print("b=足球")
print("c=羽球")  
print("d=排球")

a="籃球"
b="足球"
c="羽球"
d="排球"
w1=0
w2=0
w3=0
w4=0
allbasketball=0
allfootball=0
allbadmiton=0
allvollyball=0

ball=input("請問要借球嗎(y/n)")
while(ball == 'y'):
    p=input("請問你要借麼球:")
    if(p == '籃球'):
        w1=int(input("請問籃球要幾個"))
        allbasketball = allbasketball + w1
        a="籃球"
        print("籃球=",w1)
    elif(p == '足球'):
        w2=int(input("請問足球要幾個"))
        allfootball = allfootball + w2
        b="足球"
        print("足球=",w2)
    elif(p == '羽球'):
        w3=int(input("請問羽球要幾個"))
        allbadmiton = allbadmiton+ w3
        c="羽球"
        print("羽球=",w3)
    elif(p == '排球'):
        w4=int(input("請問排球要幾個"))
        allvollyball = allvollyball + w4
        d="排球"
    else:
        print("沒有這個球")
    ball=input("請問還要繼續借球嗎(y/n)")
    
print("借球個數:","籃球=",allbasketball,"足球=",allfootball,"羽球=",allbadmiton,"排球=",allvollyball)

