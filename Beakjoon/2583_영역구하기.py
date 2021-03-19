from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(s, e):
    global cnt
    queue = deque()
    queue.append((s, e))
    visited[s][e] = 1
    cnt += 1
    while queue:
        x, y = queue.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if not visited[nx][ny] and board[nx][ny] == 1:
                cnt += 1
                visited[nx][ny] = 1
                queue.append((nx, ny))


M, N, K = map(int, input().split())
board = [[1]*N for _ in range(M)]
visited = [[0]*N for _ in range(M)]

for k in range(K):
    a, b, c, d = map(int, input().split())
    for i in range(b, d):
        for j in range(a, c):
            board[i][j] = 0

total = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            cnt = 0
            bfs(i, j)
            total.append(cnt)

total.sort()
print(len(total))
for t in total:
    print(t, end=' ')