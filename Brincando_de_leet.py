def transforma(texto):
    numeros=('0','1','2','3','4','5','6','7','8','9')
    resposta=''
    global mudancas
    for i in range(len(texto)-1,-1,-1):
        if (texto[i] in numeros):
            mudancas=0
            break
        elif (texto[i]=='a') or (texto[i]=='A'):
            resposta+='@'
            mudancas+=1
        elif (texto[i]=='e') or (texto[i]=='E'):
            resposta+='3'
            mudancas+=1
        elif (texto[i]=='i') or (texto[i]=='I'):
            resposta+='1'
            mudancas+=1
        elif (texto[i]=='o') or (texto[i]=='O'):
            resposta+='0'
            mudancas+=1
        elif (texto[i]=='t') or (texto[i]=='T'):
            resposta+='7'
            mudancas+=1
        elif (texto[i]=='s') or (texto[i]=='S'):
            resposta+='5'
            mudancas+=1
        else:
            resposta+=texto[i]
    return resposta

frase=input()
mudancas=0
leet=transforma(frase)
if (len(frase)==0):
    print('Erro: String vazia')
    print(0)
elif (mudancas==0):
    print('numeros')
    print(0)
else:
    print(leet)
    print(mudancas)
