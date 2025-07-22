def rearrange_ele_by_sign(arr):
    pos=neg=[]
    for num in arr:
        if num>0:
            pos.append(num)
        else:
            neg.append(num)
    for i in range(0,len(pos),2):
        arr[i]=pos[i//2]
    for i in range(1,len(neg),2):
        arr[i]=neg[i-1//2]
    return arr