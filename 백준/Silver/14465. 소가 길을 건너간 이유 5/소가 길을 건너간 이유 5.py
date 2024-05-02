'''
1/ 2/ 3 4 5/ 6 7 8 9/ 10/

고장난 신호등 리스트




리스트에 포함 되어있으면 cnt 1
아니면 +1

'''


n, k, b = map(int, input().split())
lst = [0] * (n+1)
broke = [int(input()) for _ in range(b)]
for i in broke:
    lst[i] = 1

s = 1
e = k
now = 0
for i in broke:
    if s <= i <= k:
        now += 1
# print(now)
min_cnt = now
while e <= n:
    if lst[s] == 1:
        now -= 1
    s += 1
    e += 1
    if e > n:
        break
    if lst[e] == 1:
        now += 1
    if min_cnt > now:
        min_cnt = now


print(min_cnt)










