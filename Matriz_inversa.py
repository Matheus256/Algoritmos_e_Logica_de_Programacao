n=int(input())
A,B=[],[]
for i in range (n):
    linha=list(map(int,input().split()))
    A.append(linha)
for i in range (n):
    linha=list(map(int,input().split()))
    B.append(linha)
C=[]
for i in range (n):
    linha=[]
    for k in range (n):
        c=0
        for j in range (n):
            c+=A[i][j]*B[j][k]
        linha.append(c)
    C.append(linha)
for i in range (n):
    print(*C[i])
resultado=True
for i in range (n):
    for j in range (n):
        if (i==j):
            if (C[i][j]!=1):
                resultado=False
                break
        else:
            if (C[i][j]!=0):
                resultado=False
                break
    if (resultado==False):
        break
if (resultado==True):
    print("Acertou")
else:
    print("Errou")
