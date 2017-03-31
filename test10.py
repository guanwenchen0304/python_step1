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
    
