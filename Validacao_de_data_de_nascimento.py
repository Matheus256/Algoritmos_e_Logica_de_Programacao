dia=int(input())
mes_grande=("01","03","05","07","08","10","12")
mes_medio=("04","06","09","11")
if (dia>31) or (dia<1):
    print("Dia inexistente")
else:
    mes=input()
    if (mes in mes_grande):
        if (dia>0) and (dia<32):
            ano=int(input())
            if (ano>=1900) and (ano<=2020):
                print("Data Validada")
            else:
                print("Ano inexistente")
        else:
            print("Esse dia nao existe nesse mes")
    elif (mes in mes_medio):
        if (dia>0) and (dia<31):
            ano=int(input())
            if (ano>=1900) and (ano<=2020):
                print("Data Validada")
            else:
                print("Ano inexistente")
        else:
            print("Esse dia nao existe nesse mes")
    elif (mes=="02"):
        if (dia>0) and (dia<30):
            ano=int(input())
            if (ano>=1900) and (ano<=2020):
                if (ano%4==0):
                    if (ano%100!=0):
                        print("Data Validada")
                    elif (ano%400==0):
                        print("Data Validada")
                    else:
                        print("Esse ano nao eh bissexto")
                else:
                    print("Esse ano nao eh bissexto")
            else:
                print("Ano inexistente")
        else:
            print("Esse dia nao existe nesse mes")
    else:
        print("Mes inexistente")
