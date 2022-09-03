q = int(input())
lista = {}
for i in range(q):
    v = int(input())
    if(v in lista):
        lista[v] += 1
    else:
        lista[v] = 1


c = lista.keys()
c = sorted(c)

for j in c:
    print("%d aparece %d vez(es)" %(j,lista[j]))