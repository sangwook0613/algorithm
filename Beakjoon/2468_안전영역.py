dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(x, y, c):
    q = []
    q.append((x, y))
    temp[x][y] = c

    while q:
        a, b = q.pop(0)
        for dx, dy in dxy:
            nx = a + dx
            ny = b + dy
            if 0 <= nx < N and 0 <= ny < N and temp[nx][ny] < 0:
                temp[nx][ny] = c
                q.append((nx, ny))


N = int(input())
land = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
min_num = 101
for i in range(N):
    max_num = max(max_num, max(land[i]))
    min_num = min(min_num, min(land[i]))

ans = 1
rain = min_num
while rain < max_num:
    temp = [[-1]*N for _ in range(N)]
    safe_land = []
    for i in range(N):
        for j in range(N):
            if land[i][j] <= rain:
                temp[i][j] = 0
            else:
                safe_land.append((i, j))

    chk = 0
    for a, b in safe_land:
        if temp[a][b] < 0:
            chk += 1
            bfs(a, b, chk)
    ans = max(ans, chk)
    rain += 1

print(ans)