frase=input().split()
palavras=0
for palavra in frase:
    if ("."==palavra):
        continue
    else:
        palavras+=1
print(palavras)
