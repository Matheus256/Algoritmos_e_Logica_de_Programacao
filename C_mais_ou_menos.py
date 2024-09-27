DicAlimentos={
    'suco de laranja': 120,
    'morango fresco': 85,
    'mamao': 85,
    'goiaba vermelha': 70,
    'manga': 56,
    'laranja': 50,
    'brocolis': 34
}
x=DicAlimentos.get('mamao',0)
while True:
    n=int(input())
    if (n==0):
        break
    vitamina=0
    for i in range(n):
        entrada=input()
        vitamina+=DicAlimentos[entrada[2::]]*(int(entrada[0]))
    if (vitamina<110):
        print('Mais',110-vitamina,'mg')
    elif(vitamina<=130):
        print(vitamina,'mg')
    else:
        print('Menos',vitamina-130,'mg')
