dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(start):
    q = []
    for a, b in start:
        visited[a][b] = 1
        q.append((a, b))
    while q:
        a, b = q.pop(0)
        for dx, dy in dxy:
            x = a + dx
            y = b + dy
            if 0 <= x < N and 0 <= y < M and not visited[x][y] and board[x][y] == 0:
                visited[x][y] = 1
                q.append((x, y))

    total = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and board[i][j] == 0:
                total += 1
    return total


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    thins = []
    chick = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                thins.append((i, j))
            elif board[i][j] == 2:
                chick.append((i, j))

    ans = 0
    thins_len = len(thins)
    for a in range(thins_len):
        board[thins[a][0]][thins[a][1]] = 1
        for b in range(a+1, thins_len):
            board[thins[b][0]][thins[b][1]] = 1
            for c in range(b+1, thins_len):
                board[thins[c][0]][thins[c][1]] = 1
                visited = [[0]*M for _ in range(N)]
                ans = max(ans, bfs(chick))
                board[thins[c][0]][thins[c][1]] = 0
            board[thins[b][0]][thins[b][1]] = 0
        board[thins[a][0]][thins[a][1]] = 0

    print('#%d %d' % (t, ans))