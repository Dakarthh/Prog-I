op = input()
soma = 0
fora = 10
dentro = 1
dif = False

qte = 0
falso = fora
verdadeiro = dentro


for i in range(144):
	valor = float(input())

	if(i < 23):
		continue

	if (dif):
		if(falso + verdadeiro == 0):
			fora += 1
			dentro -= 1

			if(i == 79):
				dentro = 5

			falso = fora
			verdadeiro = dentro

		if (verdadeiro > 0):
			verdadeiro -= 1
			soma += valor
			qte += 1
			continue

		if (falso > 0):
			falso -= 1
			continue
		
		break
	else:
		if(falso + verdadeiro == 0):
			fora -= 1
			dentro += 1
			falso = fora
			verdadeiro = dentro	

		if (verdadeiro > 0):
			if(verdadeiro == 5):
				dif = True
				dentro = 5
				fora = 7
				falso = fora

			verdadeiro -= 1
			soma += valor
			qte += 1
			continue

		if (falso > 0):
			falso -= 1
			continue

if(op == 'S'):
	print('%.1f' %soma)
else:
	print('%.1f' %(soma/float(qte)))
