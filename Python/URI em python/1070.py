valor = int(input())

q = 0

while True:
    if(valor%2 != 0):
        q += 1
        print(valor)
    valor += 1
    if(q == 6):
        break