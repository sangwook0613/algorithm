from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque()
    queue.append((a, b, 0))
    visited[0][a][b] = 1
    visited[1][a][b] = 1
    while queue:
        x, y, jump = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                continue
            if jump == 0:
                if board[nx][ny] == 0 and visited[jump][nx][ny] == 0:
                    visited[jump][nx][ny] = visited[jump][x][y] + 1
                    queue.append((nx, ny, 0))
                if board[nx][ny] == 1 and visited[1][nx][ny] == 0:
                    visited[1][nx][ny] = visited[0][x][y] + 1
                    queue.append((nx, ny, 1))
            else:
                if board[nx][ny] == 0 and visited[jump][nx][ny] == 0:
                    visited[jump][nx][ny] = visited[jump][x][y] + 1
                    queue.append((nx, ny, 1))
    if visited[0][N-1][M-1] == 0 and visited[1][N-1][M-1] == 0:
        return -1
    else:
        if visited[0][N-1][M-1] == 0:
            return visited[1][N-1][M-1]
        if visited[1][N-1][M-1] == 0:
            return visited[0][N-1][M-1]
        return min(visited[0][N-1][M-1], visited[1][N-1][M-1])


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)]]
visited += [[[0]*M for _ in range(N)]]
print(bfs(0, 0))