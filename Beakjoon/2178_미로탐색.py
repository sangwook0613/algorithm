### DFS는 깊이가 너무 깊어지기에 시간 초과 발생 ###
# def dfs(a, b, cnt):
#     # 인덱스 범위를 벗어나면 return
#     if a < 0 or a > N-1 or b < 0 or b > M-1:
#         return
#     # 좌표 위치까지 오는데 횟수가 이전보다 많다면 return
#     if cnt > miro[a][b] and miro[a][b] != 1:
#         return
#     cnt += 1
#     if miro[a][b] >= 1 and visited[a][b] == 0:
#         miro[a][b] = cnt # 좌표에 도달하기까지 지나간 칸의 수를 채워준다.
#         visited[a][b] = 1 # 방문 표시
#         if a == N - 1 and b == M - 1:
#             visited[a][b] = 0
#             return
#         dfs(a-1, b, cnt) # 상
#         dfs(a+1, b, cnt) # 하
#         dfs(a, b-1, cnt) # 좌
#         dfs(a, b+1, cnt) # 우
#         visited[a][b] = 0 # 방문 표시 해제
from collections import deque

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                continue
            if miro[nx][ny] == 1:
                queue.append((nx, ny))
                miro[nx][ny] = miro[x][y] + 1
    return miro[N-1][M-1]


N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
print(bfs(0, 0))