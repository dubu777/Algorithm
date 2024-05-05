import sys
n, m = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
prefix = [0] * (n + 1)
for k in range(1, n + 1):
    prefix[k] = prefix[k - 1] + arr[k]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    ans = prefix[j]-prefix[i-1]
    print(ans)