n, m = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if ans < lst[i]+lst[j]+lst[k] <= m:
                ans = lst[i]+lst[j]+lst[k]
print(ans)