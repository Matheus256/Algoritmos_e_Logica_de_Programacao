L,C=map(int,input().split())
A=[]
for i in range (L):
    linha=list(map(int,input().split()))
    A.append(linha)
for i in range (C):
    if (i%2==0):
        for j in range (L):
            if (A[j][i]==0):
                print("Queria que todo mundo fosse assim")
            else:
                print("Desliga o farol cidadao ( ._.)")
    else:
        for j in range (L-1,-1,-1):
            if (A[j][i]==0):
                print("Queria que todo mundo fosse assim")
            else:
                print("Desliga o farol cidadao ( ._.)")
