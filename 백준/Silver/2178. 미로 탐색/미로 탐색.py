from collections import deque

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[n - 1][m - 1]

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
print(bfs(0, 0))
