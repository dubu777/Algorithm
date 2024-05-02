lst = sorted([int(input()) for _ in range(9)])
s = 0
e = 8
now = sum(lst) - 100

while s < e:
    if lst[s] + lst[e] < now:
        s += 1
    elif lst[s] + lst[e] > now:
        e -= 1
    else:
        for i in range(9):
            if i != s and i != e:
                print(lst[i])
        break