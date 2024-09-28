while True:
    inverso=""
    num=int(input())
    while (num<0) or (num>999):
        print("numero invalido, digite numeros de 1 a 999")
        num=int(input())
    if (num==0):
        break
    centena=num//10**2
    num=num%10**2
    dezena=num//10
    unidade=num%10
    print("O numero tem :",centena, "centenas")
    print("O numero tem :",dezena, "dezenas")
    print("O numero tem :",unidade, "unidades")
    if (centena==0):
        if (dezena==0):
            inverso=unidade
        else:
            inverso=str(unidade)+str(dezena)
    else:
        inverso=str(unidade)+str(dezena)+str(centena)
    print("O numero invertido eh: ",int(inverso))
