def dfs(s):
    global ans
    V[s] = 1
    ans += 1
    for i in adj[s]:
        if not V[i]:
            dfs(i)

v = int(input())
e = int(input())
adj = [[] for _ in range(v+1)]
for _ in range(e):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

V = [0]*(v+1)
ans = -1
dfs(1)
print(ans)