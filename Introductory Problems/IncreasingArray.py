def incArr(n):
    arr = list(map(int,input().split()))
    minMove = 0
    for i in range(1,n):
        if arr[i - 1] > arr[i]:
            minMove += arr[i - 1] - arr[i]
            arr[i] += arr[i - 1] - arr[i]
    print(minMove)

n = int(input())
incArr(n)