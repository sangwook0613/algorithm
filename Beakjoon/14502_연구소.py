from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_sum(arr):
    total = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0 and board[r][c] == 0:
                total += 1
    return total


def bfs(arr):
    queue = deque()
    for p in arr:
        queue.append((p[0], p[1]))
        visited[p[0]][p[1]] = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    return get_sum(visited)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

zeros = []
viruses = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            zeros.append((i, j))
        if board[i][j] == 2:
            viruses.append((i, j))

ans = 0
for a in range(len(zeros)):
    board[zeros[a][0]][zeros[a][1]] = 1
    for b in range(a+1, len(zeros)):
        board[zeros[b][0]][zeros[b][1]] = 1
        for c in range(b+1, len(zeros)):
            board[zeros[c][0]][zeros[c][1]] = 1
            visited = [[0]*M for _ in range(N)]
            ans = max(ans, bfs(viruses))
            board[zeros[c][0]][zeros[c][1]] = 0
        board[zeros[b][0]][zeros[b][1]] = 0
    board[zeros[a][0]][zeros[a][1]] = 0

print(ans)