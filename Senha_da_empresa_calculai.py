for i in range(5):
    nome=input()
    if (nome=='SAIR'):
        break
    else:
        nascimento=input()
        cidade=input()
        idade=input()
        print("Nome:",nome)
        print("Data de Nascimento:",nascimento)
        print("Cidade Natal:",cidade)
        print("Idade:",idade,"anos")
        senha=''
        data=nascimento[0]+nascimento[1]+nascimento[3]+nascimento[4]
        for i in range(4):
            senha+=nome[i]
            senha+=data[i]
            if (cidade[i]==" "):
                senha+=cidade[i+1]
            else:
                senha+=cidade[i]
        senha+=nome[4]+idade
        print("Senha:",senha)
        print("")
