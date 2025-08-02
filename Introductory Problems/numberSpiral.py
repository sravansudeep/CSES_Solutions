def nS(r,c):
    n = 1
    if r > c:
        if r%2 == 0:
            n = r**2 - c + 1
        else:
            n = (r-1)**2 + c
    else:
        if c%2 == 0:
            n = (c-1)**2 + r
        else:
            n = c**2 - r + 1
    print(n)

t = int(input())
while(t > 0):
    r,c = map(int,input().split())
    nS(r,c)
    t -= 1