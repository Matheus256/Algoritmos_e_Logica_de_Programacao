entrada=input()
lado=entrada[0]
tipo=entrada[2]
nome=''
for i in range (4,len(entrada)):
    nome+=entrada[i]
if (lado=="c"):
    resposta=""
    for i in range (len(nome)-1,-1,-1):
            resposta+=nome[i]
    if (tipo=='1'):
        resposta+=nome[0]*4
else:
    if (tipo=='1'):
        resposta=nome+nome[-1]*4
    else:
        resposta=nome
resposta=resposta.title()
print(resposta)
