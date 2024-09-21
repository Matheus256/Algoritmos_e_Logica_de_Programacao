entrada=(input().split(","))
cont=0
verbos,palavras=[],[]
for palavra in entrada:
    palavras.append(palavra.strip())
for palavra in palavras:
    if (palavra.endswith("r")==True):
        if (palavra.endswith("ur")==True):
            continue
        else:
            cont+=1
            verbos.append(palavra)
print("temos",cont,"palavra(s) no infitivo.")
for palavra in verbos:
    n=len(palavra)
    if (palavra.endswith("er")==True):
        print("o verbo",palavra,"no Gerundio eh:",palavra[0:n-1:1]+"ndo")
        print("o verbo",palavra,"no Participio eh:", palavra[0:n-2:1]+"ido")
        print("a vogal tematica do verbo",palavra, "eh e")
        print("o radical do verbo",palavra,"eh",palavra[0:n-2:1])
        print("O verbo",palavra,"eh da segunda conjugacao.")
    elif (palavra.endswith("ar")==True):
        print("o verbo",palavra,"no Gerundio eh:",palavra[0:n-1:1]+"ndo")
        print("o verbo",palavra,"no Participio eh:",palavra[0:n-1:1]+"do")
        print("a vogal tematica do verbo",palavra,"eh a")
        print("o radical do verbo",palavra,"eh",palavra[0:n-2:1])
        print("O verbo",palavra,"eh da primeira conjugacao.")
    elif (palavra.endswith("ir")==True):
        print("o verbo",palavra,"no Gerundio eh:",palavra[0:n-1:]+"ndo")
        print("o verbo",palavra,"no Participio eh:",palavra[0:n-1:1]+"do")
        print("a vogal tematica do verbo",palavra,"eh i")
        print("o radical do verbo",palavra,"eh",palavra[0:n-2:1])
        print("O verbo",palavra,"eh da terceira conjugacao.")
    elif (palavra.endswith("or")==True):
        print("o verbo",palavra,"no Gerundio eh:",palavra[0:n-1:1]+"ndo")
        print("o verbo",palavra,"no Participio eh:",palavra[0:n-1:1]+"sto")
        print("a vogal tematica do verbo",palavra,"eh o")
        print("o radical do verbo",palavra,"eh",palavra[0:n-2:1])
        print("O verbo",palavra,"eh da segunda conjugacao.")
    print("")
