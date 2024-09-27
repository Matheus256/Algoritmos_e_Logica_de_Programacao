alunos=[]
while True:
    aluno=input()
    if (aluno=='FIM'):
        break
    else:
        alunos+=[aluno]
tamanho=len(alunos)
notas1=[]
notas2=[]
notas3=[]
notas4=[]
for i in range (tamanho):
    notas1+=[float(input())]
for i in range (tamanho):
    notas2+=[float(input())]
for i in range (tamanho):
    notas3+=[float(input())]
for i in range (tamanho):
    notas4+=[float(input())]
medias=[]
for i in range (tamanho):
    medias+=[(notas1[i]+2*notas2[i]+3*notas3[i]+4*notas4[i])/10]
media=sum(medias)/tamanho
louvor,direto,reprovados,final=0,0,0,0
for i in range (tamanho):
    if (medias[i]>=9):
        louvor+=1
    elif (medias[i]>=7):
        direto+=1
    elif (medias[i]>=3):
        final+=1
    else:
        reprovados+=1
print("Media da turma: %.1f" %media)
print("Reprovados:",reprovados)
print("Vao para final:",final)
print("Aprovados diretamente:",direto)
print("Aprovados com louvor:",louvor)
print("")
print("Alunos acima da m�dia")
print("---------------------")
melhores=[]
notoes=[]
for j in range (tamanho):
    melhor=alunos[0]
    maior=medias[0]
    posicao=0
    for i in range (len(medias)):
        if (medias[i]>=maior):
            if (medias[i]==maior):
                if (alunos[i][0]<melhor):
                    melhor=alunos[i]
                    maior=medias[i]
                    posicao=i
            else:
                melhor=alunos[i]
                maior=medias[i]
                posicao=i
    if (maior>=media):
        melhores+=[melhor]
        notoes+=[maior]
    medias.pop(posicao)
    alunos.pop(posicao)
for i in range (len(melhores)):
    print(melhores[i].ljust(19," "),"%.1f" %notoes[i])
