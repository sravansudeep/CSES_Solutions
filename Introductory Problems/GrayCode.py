def GC(n):
    amt = pow(2,n)
    for i in range(amt):
        g = i ^ (i >> 1)
        print(format(g, f'0{n}b'))

n = int(input())
GC(n)
