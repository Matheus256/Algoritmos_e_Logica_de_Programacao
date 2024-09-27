def converte(frase):
    resposta=''
    for letra in frase:
        achou=False
        for j in range (n):
            if (letra==antigo[j]):
                resposta+=novo[j]
                achou=True
                break
            elif (letra==novo[j]):
                resposta+=antigo[j]
                achou=True
                break
        if (achou==False):
            resposta+=letra
    return resposta

n,m=map(int,input().split())
antigo,novo=[],[]
frases=[]
for i in range (n):
    entrada=input().split()
    antigo.append(entrada[0])
    novo.append(entrada[1])
for i in range (m):
    frases.append(input())
for i in range (m):
    print(converte(frases[i]))
