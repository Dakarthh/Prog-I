op = input()
soma = 0
fora = 1
dentro = 11
q = 0
falso = fora
verdadeiro = dentro

for i in range(144):
	valor = float(input())

	if(falso + verdadeiro == 0):
		fora += 1
		dentro -= 1
		falso = fora
		verdadeiro = dentro

	if (falso > 0):
		falso -= 1
		continue
	
	if (verdadeiro > 0):
		verdadeiro -= 1
		soma += valor
		q += 1
		continue
		
if(op == 'S'):
	print('%.1f' %soma)
else:
	print('%.1f' %(soma/float(q)))