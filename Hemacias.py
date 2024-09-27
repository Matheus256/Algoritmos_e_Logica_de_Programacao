def resultado(hemacias,categoria):
    if (hemacias<DicRefencia[categoria][0]):
        return 'Baixo'
    elif (hemacias<=DicRefencia[categoria][1]):
        return 'Normal'
    else:
        return 'Alto'

DicRefencia={
    'H':[4.50,6.10],
    'M':[4.00,5.40],
    'C':[4.07,5.37],
    'I':[3.90,5.36]
}
while True:
    entrada=input()
    if (entrada=='*'):
        break
    entrada=entrada.split()
    numero=float(entrada[0])
    exame=resultado(numero,entrada[1])
    if (entrada[1]=='H'):
        print('Hemacias '+'%.2f' %numero+'/mm3(Homem) = '+exame)
    elif (entrada[1]=='M'):
        print('Hemacias '+'%.2f' %numero+'/mm3(Mulher) = '+exame)
    elif (entrada[1]=='C'):
        print('Hemacias '+'%.2f' %numero+'/mm3(Crianca) = '+exame)
    else:
        print('Hemacias '+'%.2f' %numero+'/mm3(Idoso) = '+exame)
