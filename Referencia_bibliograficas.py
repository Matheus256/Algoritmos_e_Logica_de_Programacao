def referencia(posicao):
    if (posicao==n-2):
        if (nome[posicao] in conectivos):
            return nome[posicao]
        else:
            return nome[posicao].title()
    else:
        if (nome[posicao] in conectivos):
            return nome[posicao]+" "+referencia(posicao+1)
        else:
            return nome[posicao].title()+" "+referencia(posicao+1)

nome=input().split()
n=len(nome)
conectivos=("da","de","di","dos","das","e")
resposta=nome[n-1].upper()+", "+referencia(0)+"."
print(resposta)
