# 상 하 좌 우
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = int(1e9)

def dij(a, b):
    weight = [[INF]*N for _ in range(N)]
    weight[a][b] = cave[a][b]
    q = [(a, b, cave[a][b])]

    while q:
        r, c, cost = q.pop(0)
        if weight[r][c] < cost:
            continue
        for dx, dy in dxy:
            x = r + dx
            y = c + dy
            if 0 <= x < N and 0 <= y < N:
                temp = cave[x][y] + cost
                if temp < weight[x][y]:
                    weight[x][y] = temp
                    q.append((x, y, temp))

    return weight[N-1][N-1]


T = 1

while True:
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    print('Problem %d: %d' % (T, dij(0, 0)))
    T += 1