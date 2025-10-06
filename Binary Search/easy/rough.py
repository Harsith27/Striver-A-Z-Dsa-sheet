def gasstation(gas,cost):
    if sum(gas)<sum(cost):
        return -1
    total=0
    start=0
    for i in range(len(gas)):
        total+=gas[i]-cost[i]
        if total<0:
            start=i+1
            total=0     
    return start  
gas=[1,2,3,4,5]
cost=[3,4,5,1,2 ]
gasstation(gas,cost)      