def printNto1(n):
    if n==0:
        return
    printNto1(n-1)
    print(n)
n=int(input())
printNto1(n)

#****important print postition relative to recursive call

