v = int(input())
r = str(v)+'\n'

cel100 = v%100
if(cel100 == v):
    r += '%d nota(s) de R$ 100,00\n' % 0
else:
    r += '%d nota(s) de R$ 100,00\n' % (v / 100)

cel50 = cel100%50
if(cel50 == cel100):
    r += '%d nota(s) de R$ 50,00\n' % 0
else:
    r += '%d nota(s) de R$ 50,00\n' % (cel100 / 50)

cel20 = cel50%20
if(cel20 == cel50):
    r += '%d nota(s) de R$ 20,00\n' % 0
else:
    r += '%d nota(s) de R$ 20,00\n' % (cel50 / 20)

cel10 = cel20%10
if(cel10 == cel20):
    r += '%d nota(s) de R$ 10,00\n' % 0
else:
    r += '%d nota(s) de R$ 10,00\n' % (cel20 / 10)

cel5 = cel10%5
if(cel5 == cel10):
    r += '%d nota(s) de R$ 5,00\n' % 0
else:
    r += '%d nota(s) de R$ 5,00\n' % (cel10/ 5)

cel2 = cel5%2
if(cel2 == cel5):
    r += '%d nota(s) de R$ 2,00\n' % 0
else:
    r += '%d nota(s) de R$ 2,00\n' % (cel5/ 2)

cel1 = cel2%1
if(cel1 == cel2):
    r += '%d nota(s) de R$ 1,00' % 0
else:
    r += '%d nota(s) de R$ 1,00' % (cel2 / 1)

print(r)