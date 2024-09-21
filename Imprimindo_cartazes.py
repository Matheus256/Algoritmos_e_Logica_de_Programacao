tipo=int(input())
frase=input()
if (tipo==1):
    grafica1=2
    grafica2=6
else:
    grafica1=4
    grafica2=9
letras=len(frase)
if (letras<=10):
    grafica1+=letras*0.75
    grafica2+=letras*0.25
elif (letras<=30):
    grafica1+=letras*0.45
    grafica2+=letras*0.15
else:
    grafica1+=letras*0.20
    grafica2+=letras*0.10
if (grafica1<grafica2):
    print("A grafica 1 eh a mais em conta")
    print("O preco sera: $%.2f" %grafica1)
else:
    print("A grafica 2 eh a mais em conta")
    print("O preco sera: $%.2f" %grafica2)
