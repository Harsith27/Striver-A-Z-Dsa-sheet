import time
start = time.time()
arr=list(map(int,input().split()))
queries=list(map(int,input().split()))
for q in queries:
    count=0
    for num in arr:
        if q==num:
            count+=1
    print(q,"->",count)

print("Execution Time:", time.time() - start, "seconds")

    