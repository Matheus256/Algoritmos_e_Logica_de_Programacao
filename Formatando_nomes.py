conectores=('da','de','di','do','du','e')
while True:
    entrada=input()
    if (entrada=='*'):
        break
    else:
        palavras=entrada.split()
        resposta=palavras[0].capitalize()
        for i in range(1,len(palavras)):
            if (palavras[i].lower() in conectores):
                resposta+=' '+palavras[i].lower()
            else:
                resposta+=' '+palavras[i].capitalize()
        print(resposta)
