def eh_primo(num:int)->bool:
	"""
	Função que verifica se um número inteiro é primo.

	num: número inteiro
	"""
	for i in range(2,num//2):
		if(num % i == 0):
			return False
	return True

numero = int(input("Informe um número inteiro: "))

if(eh_primo(numero)):
	print("O número",numero,"é primo")
else:
	print("O número",numero,"não é primo")
