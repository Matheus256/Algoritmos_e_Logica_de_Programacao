inicio=int(input())
soma=0
while True:
    fim=int(input())
    if (fim>inicio):
        break
    else:
        print("Digite um valor maior que o primeiro!")
for numeros in range (inicio,fim+1):
    ehprimo=True
    for j in range (2,numeros):
        if (numeros%j==0):
            ehprimo=False
            break
    if (ehprimo==True):
        soma=soma+numeros
if (soma==0):
    print("Sem numeros primos no intervalo informado.")
else:
    print(soma)
