n=int(input())
numeros,nomes,notas=[],[],[]
for i in range (n):
    entrada=input().split("-")
    numeros.append(int(entrada[0]))
    nomes.append(entrada[1])
    notas.append(float(entrada[2]))
medias=[]
alunos=[]
matriculas=[]
for j in range (n):
    maior=notas[0]
    matricula=numeros[0]
    posi=0
    for i in range (1,len(notas)):
        if (notas[i]>=maior):
            if (notas[i]==maior):
                if (matricula<numeros[i]):
                    maior=notas[i]
                    matriula=numeros[i]
                    posi=i
            else:
                maior=notas[i]
                matriula=numeros[i]
                posi=i
    alunos.append(nomes[posi])
    matriculas.append(numeros[posi])
    medias.append(notas[posi])
    nomes.pop(posi)
    notas.pop(posi)
    numeros.pop(posi)
print("Alunos abaixo da media:")
ok=True
media=sum(medias)/n
for i in range (n-1,-1,-1):
    if (medias[i]>=media) and (ok==True):
        ok=False
        print("Alunos iguais ou acima da media:")
    print("Matricula:",matriculas[i],"Nome:",alunos[i],"Nota:",medias[i])
print("Media = %.2f" %media)
