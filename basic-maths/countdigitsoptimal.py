import math
def countdigits(n):
    return int(math.log10(n) + 1) #if n>0 else 1
n=int(input())
print(countdigits(n))