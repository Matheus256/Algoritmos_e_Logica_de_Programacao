n=int(input())
estatuas=[]
for i in range (n):
    estatuas+=[int(input())]
estatuas.sort()
cont=0
for i in range (n-1):
    cont+=estatuas[i+1]-estatuas[i]-1
print(cont)
