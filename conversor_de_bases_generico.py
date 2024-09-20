vezes=int(input())
for i in range (vezes):
    num=int(input())
    base=int(input())
    resultado=""
    while (num//base!=0):
        alga=num%base
        if (alga==10):
            resultado="A"+resultado
        elif (alga==11):
            resultado="B"+resultado
        elif (alga==12):
            resultado="C"+resultado
        elif (alga==13):
            resultado="D"+resultado
        elif (alga==14):
            resultado="E"+resultado
        elif (alga==15):
            resultado="F"+resultado
        else:
            resultado=str(alga)+resultado
        num=num//base
    if (num==10):
        resultado="A"+resultado
    elif (num==11):
        resultado="B"+resultado
    elif (num==12):
        resultado="C"+resultado
    elif (num==13):
        resultado="D"+resultado
    elif (num==14):
        resultado="E"+resultado
    elif (num==15):
        resultado="F"+resultado
    else:
        resultado=str(num)+resultado
    print(resultado)
