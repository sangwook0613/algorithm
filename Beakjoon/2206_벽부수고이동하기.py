# from collections import deque
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def bfs(a, b):
#     queue = deque()
#     queue.append((a, b))
#     while queue:
#         x, y = queue.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if nx < 0 or nx > N-1 or ny < 0 or ny > M-1 or board[nx][ny] != 0:
#                 continue
#             if board[nx][ny] == 0 and visited[nx][ny] == 0:
#                 visited[nx][ny] = visited[x][y] + 1
#                 queue.append((nx, ny))
#     if visited[N-1][M-1] == 0:
#         return 1000000
#     else:
#         return visited[N-1][M-1] + 1
#
#
# N, M = map(int, input().split())
# board = [list(map(int, input())) for _ in range(N)]
# ans = 1000000
# for i in range(N):
#     for j in range(M):
#         if board[i][j] == 1:
#             chk = 0
#             for c in range(4):
#                 ci = i + dx[c]
#                 cj = j + dy[c]
#                 if 0 <= ci <= N-1 and 0 <= cj <= M-1 and board[ci][cj] == 1:
#                     chk += 1
#             if chk >= 3:
#                 continue
#             visited = [[0]*M for _ in range(N)]
#             board[i][j] = 0
#             cnt = bfs(0, 0)
#             if ans > cnt:
#                 ans = cnt
#             board[i][j] = 1
# if ans == 1000000:
#     print(-1)
# else:
#     print(ans)