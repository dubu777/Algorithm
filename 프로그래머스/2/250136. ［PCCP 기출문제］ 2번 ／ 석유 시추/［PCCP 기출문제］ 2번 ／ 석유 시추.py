def solution(land):


    def find_oil(sxy):
        from collections import deque
        cnt = 1
        q = deque()
        q.append((sxy))
        col = set()
        while q:
            x, y = q.pop()
            col.add(y)
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx = dx + x
                ny = dy + y
                if 0<= nx < r and 0<= ny < c and land[nx][ny] == 1 and v[nx][ny] == 0:
                    v[nx][ny] = 1
                    q.append((nx, ny))
                    cnt += 1
        return cnt, col


    r = len(land)
    c = len(land[0])
    v = [[0] * c for _ in range(r)]
    oil_lst = [0] * c
    for i in range(r):
        for j in range(c):
            if v[i][j] == 0 and land[i][j] == 1:
                v[i][j] = 1
                cnt_o, col = find_oil((i, j))
                for o in col:
                    oil_lst[o] += cnt_o



    return max(oil_lst)
