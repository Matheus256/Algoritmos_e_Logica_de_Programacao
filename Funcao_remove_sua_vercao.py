n=int(input())
lista=[]
for i in range (n):
    lista+=[int(input())]
remover=int(input())
if (n==0):
    print("[ ]")
    print("A lista estah vazia - nao eh possivel remover elemento")
else:
    nova_lista=[]
    for i in range (n):
        if (lista[i]==remover):
            continue
        else:
            nova_lista+=[lista[i]]
    print("[",*lista,"]")
    if (len(nova_lista)==n):
        print("Nao eh possivel remover o elemento",remover)
    else:
        print("[",*nova_lista,"]")
