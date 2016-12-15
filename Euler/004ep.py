from math import sqrt
def palindrome():
    """
    A palindromic number reads the same both ways.
    The largest palindrome made from the product 
    of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the 
    product of two 3-digit numbers.
    """
    for x in range(999,100,-1):
        pal = int(str(x) + str(x)[::-1])
        for i in range(999,int(sqrt(pal)), -1):
            if pal % i == 0 and len(str(i)) > 2 and len(str(pal/i)) > 2:
                return pal, i , pal / i


if __name__ == '__main__':
    from time import time
    start = time()
    print(palindrome())
    print(time()-start)
