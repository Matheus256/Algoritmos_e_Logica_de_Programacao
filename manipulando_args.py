#Usando o args
def soma_valores(a, *args):
    return a + sum(args)
    
resultado = soma_valores(1,2,3,4,5,6,7,8)
print(resultado)

#Outro uso do args
def media_valores(a,b, *args):
    media = (a + b + sum(args))/(2 + len(args))
    return media
    
resultado = media_valores(1,1,4,2)
print(resultado)

#Trocando valores de variaveis
a, b = 1,2
print("Valor de a:",a)
print("Valor de b:",b)

a,b = b,a
print("Valor de a:",a)
print("Valor de b:",b)

#"Abrindo" uma lista
lista = [1,2,3,4,5,6,7,8]

print(*lista)

#Abrindo uma lista e passando os valores para uma função
print("Soma dos valores da lista:", soma_valores(*lista))

print("Média dos valores da lista:", media_valores(*lista))
