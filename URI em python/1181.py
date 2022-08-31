L = int(input())
op = input()  
soma = 0

for i in range(12):
    for j in range(12):
        valor = float(input())
        if(i == L):
            soma += valor
               
if(op == 'S'):
     print("%.1f" %soma)
else:
     print("%.1f" %(soma/12.0))