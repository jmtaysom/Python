def triangluar_n():
    i=0
    t=0
    while True:
        i+=1
        t+=i
        yield t

def divisor(largest):
    a = triangluar_n()
    dividers = 0
    
    while dividers < largest:
        tri = a.next()
        divisors = []
        for i in range(1,tri+1):
            if tri % i == 0:
                divisors.append(i)
        dividers = len(divisors)
    print tri

divisor(500)
