def Cp(t):
    output = []
    while t > 0:
        a,b = map(int,input().split())
        while a != 0 and b != 0:
            if a > b:
                a = a%2
                b = b - (a//2)
                if a < b:
                    b = b%2
                    a = a - (b//2)
            elif a < b:
                b = b%2
                a = a - (b//2)
            if a == 0 and b == 0:
                output.append('YES')

        t -= 1


t = int(input())
Cp(t)