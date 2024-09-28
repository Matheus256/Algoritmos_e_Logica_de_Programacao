quant=int(input())
senhas=[]
digitos=0
erro=False
for i in range (quant):
    senhas.append(input())
for senha in senhas:
    for i in range (len(senha)):
        if (senha[i].islower()==True) or (senha[i].isalnum()==False):
            erro=True
            break
        else:
            digitos+=1
    if (erro==True):
        break
if (erro==True):
    print("Alguma senha eh invalida!")
else:
    resposta=""
    for senha in senhas:
        nova=''
        for i in range (len(senha)):
            if (senha[i]=='0'):
                nova+='6'
            elif (senha[i]=='1'):
                nova+='7'
            elif (senha[i]=='2'):
                nova+='9'
            elif (senha[i]=='3'):
                nova+='8'
            elif (senha[i]=='4'):
                nova+='A'
            elif (senha[i]=='5'):
                nova+='2'
            elif (senha[i]=='6'):
                nova+='B'
            elif (senha[i]=='7'):
                nova+='F'
            elif (senha[i]=='8'):
                nova+='1'
            elif (senha[i]=='9'):
                nova+='C'
            elif (senha[i]=='A'):
                nova+='0'
            elif (senha[i]=='B'):
                nova+='D'
            elif (senha[i]=='C'):
                nova+='E'
            elif (senha[i]=='D'):
                nova+='3'
            elif (senha[i]=='E'):
                nova+='5'
            elif (senha[i]=='F'):
                nova+='4'
            else:
                nova+=senha[i]
        resposta+="-"+nova
    print(resposta+" "+str(digitos))
