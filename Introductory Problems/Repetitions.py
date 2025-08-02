def rep(s):
    ls = 1
    cs = 1
    for i in range(1,len(s)):
        if s[i - 1] == s[i]:
            cs += 1
            ls = max(ls,cs)
        else:
            cs = 1
    print(ls)

s = input().upper().strip()
if s:
    rep(s)
else:
    print(0)