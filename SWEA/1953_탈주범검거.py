dxy = [[],
       [(-1, 0), (1, 0), (0, -1), (0, 1)],
       [(-1, 0), (1, 0), (0, 0), (0, 0)],
       [(0, 0), (0, 0), (0, -1), (0, 1)],
       [(-1, 0), (0, 0), (0, 0), (0, 1)],
       [(0, 0), (1, 0), (0, 0), (0, 1)],
       [(0, 0), (1, 0), (0, -1), (0, 0)],
       [(-1, 0), (0, 0), (0, -1), (0, 0)]]


pipe = [[1, 2, 5, 6],
        [1, 2, 4, 7],
        [1, 3, 4, 5],
        [1, 3, 6, 7]
        ]


def get_sum(arr, n, m):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                cnt += 1
    return cnt


def bfs(a, b, h):
    queue = []
    queue.append((a, b, h))
    visited[a][b] = 1
    while queue:
        x, y, depth = queue.pop(-1)
        if depth == 0:
            continue
        for k in range(len(dxy[tunnel[x][y]])):
            if dxy[tunnel[x][y]][k][0] == 0 and dxy[tunnel[x][y]][k][1] == 0:
                continue
            nx = x + dxy[tunnel[x][y]][k][0]
            ny = y + dxy[tunnel[x][y]][k][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if tunnel[nx][ny] in pipe[k]:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny, depth - 1))
                elif visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny, depth - 1))


T = int(input())

for t in range(1, T+1):
    N, M, start_r, start_c, hour = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    bfs(start_r, start_c, hour - 1)

    print('#%d %d' % (t, get_sum(visited, N, M)))