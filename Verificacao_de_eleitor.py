while True:
    idade=int(input())
    if (idade<0):
        print("Voce ainda nao nasceu.")
    elif (idade==0):
        break
    elif (idade<=15):
        print("Voco nao pode votar.")
    elif (idade<=17):
        print("Na sua idade, o voto eh opcional.")
    elif (idade<=70):
        print("Voce tem a obrigatoriedade de votar.")
    else:
        print("Na sua idade, o voto eh opcional.")
