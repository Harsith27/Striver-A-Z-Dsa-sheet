def policeman(arr,k):
    count=0
    polices=[]
    theives=[]
    for i in range(arr):
        if arr[i] == 'P':
            polices.append(i)
        else:
            theives.append(i)                                       #Optimized approach O(n)
    while i<len(polices) and j<len(theives):
        if abs(polices[i]-theives[j]) <= k:
            i+=1
            j+=1
            count+=1
        elif polices[i] < theives[j]:
            i+=1
        else:
            j+=1
    return count

arr=list(map(str,input().split()))
k=int(input())
print(policeman(arr,k))

# there is also a brute force approach which is O(n^2) where we check for each police and theif if they can catch each other or not by moving from i-k to i+k and checking if there is a theif or not and mark the caught theif so that no two polices can catch the same theif. But this is not efficient for large inputs.