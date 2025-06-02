def printNto1(n):
    if n==0:
        return
    print(n)
    printNto1(n-1)

n=int(input())
printNto1(n)

#****important print postition relative to recursive call