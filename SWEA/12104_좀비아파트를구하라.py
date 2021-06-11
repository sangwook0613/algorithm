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
            if 0 <= x < H and 0 <= y < N and 0 <= z < M and house[x][y][z] == -1:
                house[x][y][z] = 1
                q.append((x, y, z, cnt + 1))
                total = max(cnt+1, total)
    return total


T = int(input())

for t in range(1, T+1):
    M, N, H = map(int, input().split())
    house = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

    vaccines = []
    zombie_cnt = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if house[h][n][m] == 1:
                    vaccines.append((h, n, m, 0))
                elif house[h][n][m] == -1:
                    zombie_cnt += 1

    if zombie_cnt == 0:
        print('#%d ALL HUMANS' % t)
    else:
        ans = bfs(vaccines)
        leftover_zombie_chk = 0
        for h in range(H):
            for n in range(N):
                for m in range(M):
                    if house[h][n][m] == -1:
                        leftover_zombie_chk = 1
                        break
                if leftover_zombie_chk:
                    break
            if leftover_zombie_chk:
                break
        if leftover_zombie_chk:
            print('#%d STILL ZOMBIES' % t)
        else:
            print('#%d %d' % (t, ans))