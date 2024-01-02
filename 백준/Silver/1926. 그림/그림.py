from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    cnt = 1
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                q.append((nx, ny))
    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
max_size = 0
count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count += 1
            max_size = max(bfs(i, j), max_size)
print(count)
print(max_size)
