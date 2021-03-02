from collections import deque

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(arr):
    queue = deque()
    for x, y in arr:
        queue.append((x, y))
    cnt = 0
    while queue:
        a, b = queue.popleft()
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if tomato[nx][ny] == 0:
                queue.append((nx, ny))
                tomato[nx][ny] = tomato[a][b] + 1
                cnt = tomato[nx][ny]
    if cnt > 0:
        return cnt-1
    else:
        return cnt


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
ripe = []
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            ripe.append((i, j))

ans = bfs(ripe)
chk = 0
for i in range(N):
    if 0 in tomato[i]:
        chk = 1

if chk:
    print(-1)
else:
    print(ans)