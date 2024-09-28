vingador=input()
if (vingador=='Capitao America'):
    poder=input()
    energia=int(input())
    if (poder=='Escudo'):
        if (energia>=7):
            print(vingador,"conseguiu derrotar Thanos")
        else:
            print(vingador,"NAO conseguiu derrotar Thanos, chamem outro Vingador")
    else:
        print(vingador,"NAO conseguiu derrotar Thanos")
        if (poder=='Armadura de Ferro'):
            print("Esse eh o poder do Homem de Ferro")
        elif (poder=='Forca Bruta'):
            print("Esse eh o poder do Hulk")
        elif (poder=='Martelo'):
            print("Esse eh o poder do Thor")
        elif (poder=='Arco e Flecha'):
            print("Esse eh o poder do Gaviao Arqueiro")
        elif (poder=='Inteligencia'):
            print("Esse eh o poder da Viuva Negra")
elif (vingador=='Homem de Ferro'):
    poder=input()
    energia=int(input())
    if (poder=='Armadura de Ferro'):
        if (energia>=10):
            print(vingador,"conseguiu derrotar Thanos")
        else:
            print(vingador,"NAO conseguiu derrotar Thanos, chamem outro Vingador")
    else:
        print(vingador,"NAO conseguiu derrotar Thanos")
        if (poder=='Escudo'):
            print("Esse eh o poder do Capitao America")
        elif (poder=='Forca Bruta'):
            print("Esse eh o poder do Hulk")
        elif (poder=='Martelo'):
            print("Esse eh o poder do Thor")
        elif (poder=='Arco e Flecha'):
            print("Esse eh o poder do Gaviao Arqueiro")
        elif (poder=='Inteligencia'):
            print("Esse eh o poder da Viuva Negra")
elif (vingador=='Hulk'):
    poder=input()
    energia=int(input())
    if (poder=='Forca Bruta'):
        if (energia>=5):
            print(vingador,"conseguiu derrotar Thanos")
        else:
            print(vingador,"NAO conseguiu derrotar Thanos, chamem outro Vingador")
    else:
        print(vingador,"NAO conseguiu derrotar Thanos")
        if (poder=='Escudo'):
            print("Esse eh o poder do Capitao America")
        elif (poder=='Armadura de Ferro'):
            print("Esse eh o poder do Homem de Ferro")
        elif (poder=='Martelo'):
            print("Esse eh o poder do Thor")
        elif (poder=='Arco e Flecha'):
            print("Esse eh o poder do Gaviao Arqueiro")
        elif (poder=='Inteligencia'):
            print("Esse eh o poder da Viuva Negra")
elif (vingador=='Hulk'):
    poder=input()
    energia=int(input())
    if (poder=='Forca Bruta'):
        if (energia>=5):
            print(vingador,"conseguiu derrotar Thanos")
        else:
            print(vingador,"NAO conseguiu derrotar Thanos, chamem outro Vingador")
    else:
        print(vingador,"NAO conseguiu derrotar Thanos")
        if (poder=='Escudo'):
            print("Esse eh o poder do Capitao America")
        elif (poder=='Armadura de Ferro'):
            print("Esse eh o poder do Homem de Ferro")
        elif (poder=='Martelo'):
            print("Esse eh o poder do Thor")
        elif (poder=='Arco e Flecha'):
            print("Esse eh o poder do Gaviao Arqueiro")
        elif (poder=='Inteligencia'):
            print("Esse eh o poder da Viuva Negra")
elif (vingador=='Thor'):
    poder=input()
    energia=int(input())
    if (poder=='Martelo'):
        if (energia>=4):
            print(vingador,"conseguiu derrotar Thanos")
        else:
            print(vingador,"NAO conseguiu derrotar Thanos, chamem outro Vingador")
    else:
        print(vingador,"NAO conseguiu derrotar Thanos")
        if (poder=='Escudo'):
            print("Esse eh o poder do Capitao America")
        elif (poder=='Armadura de Ferro'):
            print("Esse eh o poder do Homem de Ferro")
        elif (poder=='Forca Bruta'):
            print("Esse eh o poder do Hulk")
        elif (poder=='Arco e Flecha'):
            print("Esse eh o poder do Gaviao Arqueiro")
        elif (poder=='Inteligencia'):
            print("Esse eh o poder da Viuva Negra")
elif (vingador=='Gaviao Arqueiro'):
    poder=input()
    energia=int(input())
    if (poder=='Arco e Flexa'):
        if (energia>=12):
            print(vingador,"conseguiu derrotar Thanos")
        else:
            print(vingador,"NAO conseguiu derrotar Thanos, chamem outro Vingador")
    else:
        print(vingador,"NAO conseguiu derrotar Thanos")
        if (poder=='Escudo'):
            print("Esse eh o poder do Capitao America")
        elif (poder=='Armadura de Ferro'):
            print("Esse eh o poder do Homem de Ferro")
        elif (poder=='Forca Bruta'):
            print("Esse eh o poder do Hulk")
        elif (poder=='Martelo'):
            print("Esse eh o poder do Thor")
        elif (poder=='Inteligencia'):
            print("Esse eh o poder da Viuva Negra")
elif (vingador=='Viuva Negra'):
    poder=input()
    energia=int(input())
    if (poder=='Inteligencia'):
        if (energia>=20):
            print(vingador,"conseguiu derrotar Thanos")
        else:
            print(vingador,"NAO conseguiu derrotar Thanos, chamem outro Vingador")
    else:
        print(vingador,"NAO conseguiu derrotar Thanos")
        if (poder=='Escudo'):
            print("Esse eh o poder do Capitao America")
        elif (poder=='Armadura de Ferro'):
            print("Esse eh o poder do Homem de Ferro")
        elif (poder=='Forca Bruta'):
            print("Esse eh o poder do Hulk")
        elif (poder=='Arco e Flecha'):
            print("Esse eh o poder do Gaviao Arqueiro")
        elif (poder=='Martelo'):
            print("Esse eh o poder do Thor")
else:
    print("Vingador Invalido")
