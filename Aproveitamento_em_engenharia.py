gabarito=input()
quant=int(input())
nomes=[]
provas=[]
for i in range (quant):
    nomes.append(input())
    provas.append(input())
notas,algo=[],[]
maior1,maior2=0,0
for i in range (quant):
    acerto,algoritmos=0,0
    for j in range (12):
        if (provas[i][j]==gabarito[j]):
            acerto+=1
            if (j==6) or (j==7):
                algoritmos+=1
    aux=acerto*100/12
    if (aux>maior1):
        maior1=aux
        pos=i
    notas.append(aux)
    aux1=algoritmos*50
    if (aux1>maior2):
        maior2=aux1
        posi=i
media=sum(notas)/quant
print("%.2f" %media,"%")
print(nomes[pos].upper())
print("%.2f" %notas[pos],"%")
print(nomes[posi].upper())
print("%.2f" %maior2,"%")
