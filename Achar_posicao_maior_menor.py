numeros=[]
cont=0
while True:
    num=int(input())
    while (num==0):
        if (cont>2):
            break
        else:
            print("voce deve digitar pelo menos 3 numeros antes do 0.")
            num=int(input())
    if (num==0) and (cont>=3):
        break
    while (num in numeros):
        print("numero ja existe na lista, tente outro.")
        num=int(input())
    numeros+=[num]
    cont+=1
print(numeros)
maior=max(numeros)
menor=min(numeros)
print("o maior elemento da lista eh:",maior,"e ele se encontra na posicao:",numeros.index(maior))
print("o menor elemento da lista eh:",menor,"e ele se encontra na posicao:",numeros.index(menor))
