from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            res.append(bfs(i, j))
res.sort()
print(len(res), *res, sep='\n')