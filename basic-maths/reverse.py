def reverse(n):
    temp=n
    rev=0
    while(temp>0):
        p=temp%10
        rev=rev*10 + p
        temp=temp//10
    return rev

n=int(input())
print(reverse(n))


#alternate method(using string methods)
# 
# n=int(input())
# print(int(str(n)[::-1]))