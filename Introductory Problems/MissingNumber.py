def mn(n):
    sum_ = 0 
    nums = list(map(int, input().split())) # read multiple values from a single line
    sum_ = sum(nums)
    mn = n*(n+1)//2 - sum_
    print(mn)
    
mn(int(input()))