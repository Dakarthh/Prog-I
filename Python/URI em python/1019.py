v = int(input())
hr = int(v/60/60)
min = int((v / 60) - (hr * 60))
sec = int(v - ((hr*60*60) + (min * 60)))
print(str(hr)+':'+str(min)+':'+str(sec))