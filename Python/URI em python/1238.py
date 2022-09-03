cont = 0
q = int(input())

while cont < q:
    l = input().split()
    p1 = l[0]
    p2 = l[1]
    pf = ""
    cont2 = 0

    while cont2 < len(p1) and cont2 < len(p2):
        pf += p1[cont2] + p2[cont2]
        cont2 += 1

    if cont2 < len(p1):
        pf+= p1[cont2:]

    if cont2 < len(p2):
        pf += p2[cont2:]
    

    print(pf)
    cont += 1