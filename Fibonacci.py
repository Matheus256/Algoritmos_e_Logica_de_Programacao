while True:
    num=int(input())
    a=0
    b=1
    resposta=str(a)+" "+str(b)
    if (num==0):
        break
    elif (num==1):
        print(0)
    elif (num==2):
        print(resposta)
    else:
        for i in range (2,num):
            c=a+b
            a=b
            b=c
            resposta=resposta+" "+str(b)
        print(resposta)
