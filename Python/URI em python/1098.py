i = 0
j = 1
val = 0
t1 = 0
t2 = 0

while(i <= 2):
    if(t2 == 0):
        print("I=%.0f J=%.0f" %(i,j))
    else:
        print("I=%.1f J=%.1f" %(i, j))
    
    t1 += 1
    if(t1 == 3):
        i += 0.2
        val += 0.2
        j = val
        t1 = 0
        t2 += 1

    if(t2 == 5):
        t2 = 0
    j += 1