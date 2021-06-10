from collections import deque

dxyz = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def bfs(start):
    q = deque()
    for s in start:
        q.append(s)
    total = 0
    while q:
        a, b, c, cnt = q.popleft()
        for dx, dy, dz in dxyz:
            x = a + dx
            y = b + dy
            z = c + dz
            if 0 <= x < H and 0 <= y < N and 0 <= z < M and tomato[x][y][z] == 0:
                tomato[x][y][z] = 1
                q.append((x, y, z, cnt + 1))
                total = max(cnt+1, total)
    return total


M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

points = []
zero_cnt = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1:
                points.append((h, n, m, 0))
            elif tomato[h][n][m] == 0:
                zero_cnt += 1

if zero_cnt == 0:
    print(0)
else:
    ans = bfs(points)
    zero_chk = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato[h][n][m] == 0:
                    zero_chk = 1
                    break
            if zero_chk:
                break
        if zero_chk:
            break
    if zero_chk:
        print(-1)
    else:
        print(ans)