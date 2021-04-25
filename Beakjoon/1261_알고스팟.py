dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dij(a, b):
    weight = [[10000]*M for _ in range(N)]
    weight[0][0] = 0
    q = [(a, b, 0)]

    while q:
        x, y, cost = q.pop(0)
        if weight[x][y] < cost:
            continue
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                temp = int(maze[x][y]) + cost
                if weight[nx][ny] > temp:
                    weight[nx][ny] = temp
                    q.append((nx, ny, temp))

    return weight[N-1][M-1]


M, N = map(int, input().split())
maze = [input() for _ in range(N)]
print(dij(0, 0))