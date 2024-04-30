n = int(input())
lst = sorted(list(map(int, input().split())))

ans = 0
m = len(lst)//2
if len(lst)%2 == 0:
    ans = lst[m-1]
else:
    ans = lst[m]
print(ans)