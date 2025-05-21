def print1toN(n,t):
    if t>n:
        return
    print(t)
    print1toN(n,t+1)

n=int(input())
print1toN(n,1)


#another version 
# note : default value t=1 is only set when the parameter t is not called in the func call like the print1toN(n)
#def print1toN(n,t=1):
#    if t>n:
#        return
#    print(t)
#    print1toN(n,t+1)
#
#n=int(input())
#print1toN(n)