import random

#Altere aqui para dificultar o jogo
max_valor = 21
tentativas = 3

#Função para validação da entrada 
def ler_entrada_valida()->int:
    """
    Função para validar a entrada do usuário e retornar a entrada conforme é desejado
    """
    while True:
        try:
            entrada = int(input("Tente um número inteiro: "))
        except ValueError as err:
            print("Valor inválido!")
            continue
        
        if 1 <= entrada <= max_valor:
            return entrada
            
        print("O valor deve estar entre 1 e", max_valor)
    
#Sorteio do valor
alvo = random.randint(1,max_valor)

for i in range(tentativas):
	entrada_usuario = ler_entrada_valida()
	
	if(entrada_usuario > alvo):
	    print("O número secreto é menor do que", entrada_usuario)
	elif(entrada_usuario < alvo):
	    print("O número secreto é maior do que", entrada_usuario)
	else:
	    print("Parabéns! Você acertou o número secreto!!")
	    break
else:
    print("Infelizmente suas tentativas acabaram")
    print("O número secreto era:", alvo)
