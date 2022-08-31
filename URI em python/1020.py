v = int(input())
a = int(v / 365)
m = int((v%365/30))
d = int(v%365%30)

print('%d ano(s)\n%d mes(es)\n%d dia(s)' %(a,m,d))