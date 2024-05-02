n = int(input())
lst = sorted(list(map(int, input().split())))
x = int(input())

s = 0
e = n-1
cnt = 0
while s < e:
    now = lst[s] + lst[e]
    if now == x:
        s += 1
        e -= 1
        cnt += 1
    elif now > x:
        e -= 1
    else:
        s += 1

print(cnt)