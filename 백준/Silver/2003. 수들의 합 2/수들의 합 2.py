n, m = map(int, input().split())
lst = list(map(int, input().split()))

s = 0
e = 0
now = lst[s]
cnt = 0
while e < n:
    if now < m:
        e += 1
        if e == n:
            break
        now += lst[e]
    elif now > m:
        now -= lst[s]
        s += 1
    else:
        cnt += 1
        now -= lst[s]
        s += 1
        e += 1
        if e == n:
            break
        now += lst[e]

print(cnt)
