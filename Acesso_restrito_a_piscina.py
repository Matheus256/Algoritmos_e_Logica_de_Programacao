max_criancas=int(input())
total_adultos=0
criancas_residentes=0
criancas_convidadas=0
total_criancas=0
while True:
    adultos=int(input())
    if (adultos<0):
        break
    residentes=int(input())
    convidados=int(input())
    if (total_criancas+residentes+convidados<=max_criancas) or ((residentes+convidados)==0):
        total_adultos+=adultos
        criancas_residentes+=residentes
        total_criancas+=residentes+convidados
        print("Acesso permitido!")
        print("Adultos na piscina:",total_adultos)
        print("Criancas na piscina:",total_criancas)
    elif (convidados!=0):
        total_adultos+=adultos
        criancas_residentes+=residentes
        total_criancas+=residentes+convidados
        print("Acesso permitido devido a presenca de convidado(s).")
        print("Adultos na piscina:",total_adultos)
        print("Criancas na piscina:",total_criancas)
    else:
        print("Capacidade maxima de criancas atingida/excedida.")
        print("Tem",total_criancas-max_criancas, "crianca(s) a mais que as",max_criancas,"permitidas.")
        print("Adultos na piscina:",total_adultos)
        print("Criancas na piscina:",total_criancas)
    print("***")
