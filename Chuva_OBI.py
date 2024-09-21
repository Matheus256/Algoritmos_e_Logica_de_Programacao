n=int(input())
piscina=[]
for i in range (n):
    piscina.append(int(input()))
L=[]
inicio=piscina[0]
for i in range (1,n-1):
    if (piscina[i]<inicio):
        L.append(True)
    else:
        L.append(False)
        inicio=piscina[i]
fim=piscina[n-1]
R=[]
for i in range (n-2,0,-1):
    if (piscina[i]<fim):
        R.append(True)
    else:
        R.append(False)
        fim=piscina[i]
secoes=0
R.reverse()
for i in range (len(R)):
    if (L[i]==True) and (R[i]==True):
        secoes+=1
print(secoes)
