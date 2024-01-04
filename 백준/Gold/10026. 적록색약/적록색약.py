import sys


def search(graph):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    visited = [[0 for j in range(N)] for i in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                stack = [(i, j)]
                visited[i][j] = 1
                while stack:
                    y, x = stack.pop()
                    for idx in range(4):
                        new_y, new_x = y + dy[idx], x + dx[idx]
                        if 0 <= new_y < N and 0 <= new_x < N and visited[new_y][new_x] == 0:
                            if graph[y][x] == graph[new_y][new_x]:
                                stack.append((new_y, new_x))
                                visited[new_y][new_x] = 1
                ans += 1
    return ans


N = int(sys.stdin.readline())
paint = []
for i in range(N):
    line = list(sys.stdin.readline().strip())
    paint.append(line)
key1 = search(paint)

for i in range(N):
    for j in range(N):
        if paint[i][j] == "R":
            paint[i][j] = "G"
key2 = search(paint)

print(key1, key2)