import sys


n, k = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))

prefix = [0] * (n+1)

for i in range(1, n+1):
    prefix[i] = prefix[i-1]+arr[i]

max_tem = -100000000000000

for i in range(k, n+1):
    max_tem = max(prefix[i] - prefix[i-k], max_tem)

print(max_tem)
