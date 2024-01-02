from collections import deque

def bfs(x, y):
    q = deque([[x, y]])
    graph[x][y] = -1
    while q:
        x, y = q.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = -1
                q.append([nx, ny])
    return

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)