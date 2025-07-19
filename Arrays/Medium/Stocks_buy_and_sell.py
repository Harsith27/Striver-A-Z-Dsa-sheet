def Stocks_buy_and_sell(arr):
    j=0
    max_profit=0
    for i in range(len(arr)):
        if arr[i]-arr[j] > max_profit:
            max_profit=arr[i]-arr[j]
        if arr[i]<arr[j]:
            j=i
    return max_profit
arr=list(map(int, input().split()))
print(Stocks_buy_and_sell(arr))