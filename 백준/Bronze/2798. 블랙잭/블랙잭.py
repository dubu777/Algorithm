from itertools import permutations

n, m = map(int, input().split())
lst = list(map(int, input().split()))
res = 0
for num in permutations(lst, 3):
    if sum(num) > m:
        continue
    if res < sum(num):
        res = sum(num)

print(res)
