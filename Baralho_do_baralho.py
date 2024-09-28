def pontuacao(cartas):
    pontos=0
    cartas.sort()
    if (cartas[0]==cartas[1]):
        if (cartas[1]==cartas[2]):
            pontos+=cartas[0]
        else:
            pontos+=int(cartas[0]/2)
    elif (cartas[1]==cartas[2]):
        if (cartas[1]==cartas[0]):
            pontos+=cartas[1]
        else:
            pontos+=int(cartas[1]/2)
    elif (cartas[0]==cartas[2]):
        if (cartas[1]==cartas[2]):
            pontos+=cartas[1]
        else:
            pontos+=int(cartas[2]/2)
    if (cartas[2]-cartas[1]==1) and (cartas[1]-cartas[0]==1):
        pontos+=cartas[0]
    if (sum(cartas)==8):
        pontos+=8
    return pontos
    
jogador1=list(map(int,input().split()))
jogador2=list(map(int,input().split()))
paes=pontuacao(jogador1)
willy=pontuacao(jogador2)
if (paes>willy):
    print(1)
elif (willy>paes):
    print(2)
else:
    print(0)
