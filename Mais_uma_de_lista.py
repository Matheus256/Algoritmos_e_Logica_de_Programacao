n=int(input())
if (n<0):
    print("O valor informado para N foi negativo")
elif (n==0):
    print("Lista vazia - O valor de S eh zero")
else:
    numeros=[]
    soma=0
    for i in range (n):
        numeros+=[int(input())]
    if (n%2==0):
        m=int(n/2)
        for i in range (m):
            soma+=(numeros[i]-numeros[n-i-1])**2
    else:
        m=int((n-1)/2)
        for i in range(m):
            soma+=(numeros[i]-numeros[n-i-1])**2
        soma+=numeros[m]**2
    print("S =",soma)
