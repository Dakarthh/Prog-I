import math
n1 = input().split(" ")
n2 = input().split(" ")
x1,y1 = n1
x2,y2 = n2
d = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))
print("%0.4f" %d)