def Tz(n):
    count = 0
    while n > 0:
        n = n // 5
        count += n
    print(count)
n = int(input())
Tz(n)