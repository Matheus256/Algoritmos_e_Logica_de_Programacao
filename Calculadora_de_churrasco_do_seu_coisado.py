carne=input()
if (carne=='C'):
    pao_alho=input()
    bebida_adulto=input()
    bebida_crianca=input()
    criancas=int(input())
    adultos=int(input())
    if (bebida_adulto=='S'):
        if (bebida_crianca=='S'):
            total=(25.7*adultos+criancas*9.4)
        else:
            total=(25.7*adultos+criancas*6.4)
    else:
        if (bebida_crianca=='S'):
            total=(9.7*adultos+criancas*9.4)
        else:
            total=(9.7*adultos+criancas*6.4)
    if (pao_alho=='S'):
        print("R$: %.2f" %total)
    else:
        print("R$: %.2f" %(total*0.98))
elif (carne=='BF'):
    pao_alho=input()
    bebida_adulto=input()
    bebida_crianca=input()
    criancas=int(input())
    adultos=int(input())
    if (bebida_adulto=='S'):
        if (bebida_crianca=='S'):
            total=(26.7*adultos+criancas*9.4)
        else:
            total=(26.7*adultos+criancas*6.4)
    else:
        if (bebida_crianca=='S'):
            total=(10.7*adultos+criancas*9.4)
        else:
            total=(10.7*adultos+criancas*6.4)
    if (pao_alho=='S'):
        print("R$: %.2f" %total)
    else:
        print("R$: %.2f" %(total*0.98))
elif (carne=='BS'):
    pao_alho=input()
    bebida_adulto=input()
    bebida_crianca=input()
    criancas=int(input())
    adultos=int(input())
    if (bebida_adulto=='S'):
        if (bebida_crianca=='S'):
            total=(26.25*adultos+criancas*9.4)
        else:
            total=(26.25*adultos+criancas*6.4)
    else:
        if (bebida_crianca=='S'):
            total=(10.25*adultos+criancas*9.4)
        else:
            total=(10.25*adultos+criancas*6.4)
    if (pao_alho=='S'):
        print("R$: %.2f" %total)
    else:
        print("R$: %.2f" %(total*0.98))
else:
    print("Opcao invalida.")
