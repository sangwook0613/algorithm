dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


T = int(input())


def bfs(a, b, chk):
    queue = []
    queue.append((a, b))
    chk[a][b] = 1
    cnt = 1000
    while queue:
        x, y = queue.pop(-1)
        if board[x][y] == 'W':
            if cnt > chk[x][y]-1:
                cnt = chk[x][y]-1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not chk[nx][ny]:
                chk[nx][ny] = chk[x][y] + 1
                queue.append((nx, ny))
    return cnt


for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'L':
                visited = [[0]*M for _ in range(N)]
                ans += bfs(i, j, visited)

    print('#%d %d' % (t, ans))