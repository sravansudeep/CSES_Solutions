def palinReorder(n):
    dict_ = {}; oc = 0 # counting odd
    for i in n:
        dict_[i] = dict_.get(i,0) + 1

    fh = [] # First Half
    sh = [] # Secound Half
    op = '' # odd Part
    for l,c in dict_.items():
        if c%2 == 0:
            half = l * (c//2)
            fh.append(half)
            sh.append(half)
        else:
            op = l * c
            oc += 1
    if oc > 1:
            return 'NO SOLUTION'
    return ''.join(fh) + op + ''.join(reversed(sh))

n = input()
SolutionValue = palinReorder(n)
print(SolutionValue)
