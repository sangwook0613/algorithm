# 백준 5547 일루미네이션
## 그림에서 좌표값을 달아준게 큰 힌트
dxy_even = [(1, 0), (1, -1), (-1, 0), (-1, -1), (0, 1), (0, -1)] # 짝수 줄과 연결된 경우
dxy_odd = [(1, 0), (1, 1), (-1, 0), (-1, 1), (0, 1), (0, -1)] # 홀수 줄과 연결된 경우

def find_surround(start):
    q = [start]
    nothing_visited[start[0]][start[1]] = 1
    while q:
        a, b = q.pop(0)
        if a % 2:
            for dx, dy in dxy_even:
                x = a + dx
                y = b + dy
                if 0 <= x < N and 0 <= y < M and not nothing_visited[x][y] and board[x][y] == 0:
                    nothing_visited[x][y] = 1
                    q.append((x, y))
                    board[x][y] = 2
        else:
            for dx, dy in dxy_odd:
                x = a + dx
                y = b + dy
                if 0 <= x < N and 0 <= y < M and not nothing_visited[x][y] and board[x][y] == 0:
                    nothing_visited[x][y] = 1
                    q.append((x, y))
                    board[x][y] = 2


def bfs(start):
    q = [start]
    visited[start[0]][start[1]] = 1
    chk = 0
    while q:
        a, b = q.pop(0)
        temp = []
        if a % 2:
            for dx, dy in dxy_even:
                x = a + dx
                y = b + dy
                if 0 <= x < N and 0 <= y < M and not visited[x][y] and board[x][y] == 1:
                    visited[x][y] = 1
                    chk += 1
                    temp.append((x, y))
        else:
            for dx, dy in dxy_odd:
                x = a + dx
                y = b + dy
                if 0 <= x < N and 0 <= y < M and not visited[x][y] and board[x][y] == 1:
                    visited[x][y] = 1
                    chk += 1
                    temp.append((x, y))
        print('bfs', a, b, chk, temp)
        q.extend(temp)
    return chk


M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
nothing = []
nothing_visited = [[0]*M for _ in range(N)]
walls = []
walls_visited = [[0]*M for _ in range(N)]
total = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            walls.append((i, j))
        else:
            if board[i][j] == 0 and not nothing_visited[i][j] and (i == 0 or j == 0 or i == N-1 or j == M-1):
                find_surround((i, j))

for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and nothing_visited[i][j] == 0:
            nothing.append((i, j))
print(nothing)
print(walls)
visited = [[0]*M for _ in range(N)]
for wall in walls:
    temp = bfs(wall)
    total += temp
    print(wall, temp)
print(total)
