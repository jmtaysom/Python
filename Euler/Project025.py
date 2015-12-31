a,b = 1,1
counter = 1
while len(str(a))<1000:
    a,b = b,a+b
    counter +=1
print counter
