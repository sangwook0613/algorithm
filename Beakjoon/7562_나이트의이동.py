from collections import deque
# 1시 2시 4시 5시 7시 8시 10시 11시
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1
    while queue:
        x, y = queue.popleft()
        if x == end[0] and y == end[1]:
            return visited[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


T = int(input())

for t in range(T):
    N = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    visited = [[0]*N for _ in range(N)]
    print(bfs(start[0], start[1]))