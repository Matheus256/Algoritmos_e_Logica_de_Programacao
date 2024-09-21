idade=int(input())
if (idade<=2):
    print("O individuo eh um Bebe Jovem Menor de Idade.")
elif (idade<=12):
    print("O individuo eh uma Crianca Jovem Menor de Idade.")
elif (idade<18):
    print("O individuo eh um Adolescente Jovem Menor de Idade.")
elif (idade<=19):
    print("O individuo eh um Jovem Maior de Idade.")
elif (idade<=45):
    print("O individuo eh um Adulto Maior de Idade.")
elif (idade<=59):
    print("O individuo eh um Adulto de Meia Idade Maior de Idade.")
elif (idade<=75):
    print("O individuo eh um Idoso Maior de Idade.")
elif (idade<=90):
    print("O individuo eh um Idoso Ansiao Maior de Idade.")
else:
    print("O individuo eh um Idoso na Velhice Extrema Maior de Idade.")
