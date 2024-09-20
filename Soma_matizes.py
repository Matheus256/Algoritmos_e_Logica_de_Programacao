L,C=map(int,input().split())
A=[]
B=[]
for i in range (L):
    linha=list(map(int,input().split()))
    A.append(linha)
for i in range (L):
    linha=list(map(int,input().split()))
    B.append(linha)
M=[]
for i in range (L):
    linha=[]
    for j in range (C):
        linha.append(A[i][j]+B[i][j])
    M.append(linha)
for i in range (L):
    print(*M[i])
