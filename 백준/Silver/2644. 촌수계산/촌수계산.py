def bfs(s, e):
    q = []
    v = [0] * (n + 1)
    q.append(s)
    v[s] = 1
    while q:
        c = q.pop(0)
        if c == e:
            return v[e] - 1

        for i in adj[c]:
            if not v[i]:
                v[i] = v[c] + 1
                q.append(i)
    return -1

n = int(input())
x, y = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n+1)]

cnt = 0
for _ in range(m):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

ans = bfs(x, y)
print(ans)
