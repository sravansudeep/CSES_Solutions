def bp(n):
    odd = list(range(2,n + 1, 2))
    even = list(range(1,n + 1,2))
    print(*odd + even)
n = int(input())
if n == 3 or n == 2:
    print('NO SOLUTION')
else:
    bp(n)
