dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(a, b):
    max_cnt = 0
    q = [(a, b, 0)]
    visited[a][b] = 1

    while q:
        x, y, cnt = q.pop(0)
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 'L':
                visited[nx][ny] = 1
                q.append((nx, ny, cnt+1))
                max_cnt = max(max_cnt, cnt+1)
    return max_cnt


N, M = map(int, input().split())
board = [input() for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            visited = [[0]*M for _ in range(N)]
            ans = max(ans, bfs(i, j))
print(ans)