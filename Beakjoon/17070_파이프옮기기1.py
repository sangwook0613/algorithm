# dxy = [[(0, 1), (1, 1), (-1, -1)],
#        [(0, 1), (1, 1), (1, 0)],
#        [(-1, -1), (1, 1), (1, 0)]]
#
#
# def check_wall(a, b, c, d):
#     for i in range(c + 1):
#         for j in range(d + 1):
#             if board[a + i][b + j] != 0:
#                 return False
#     return True


# def move_pipe(a, b, direction):
#     global cnt
#     if a == N-1 and b == N-1:
#         cnt += 1
#         return
#     for k in range(3):
#         dx, dy = dxy[direction][k]
#         if dx < 0 or dy < 0:
#             continue
#         x = a + dx
#         y = b + dy
#         if x >= N or y >= N:
#             continue
#         if check_wall(a, b, dx, dy):
#             move_pipe(x, y, k)
#
#
# N = int(sys.stdin.readline())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# cnt = 0
# move_pipe(0, 1, 0)
# print(cnt)

import sys

# 위에 주석처리된 코드처럼 for문을 활용하여 브루트포스 방식으로 풀려고 했으나,
# 파이썬이 워낙 느린 언어이기에 for문을 제거하고 모두 if문 처리하여 풀었다.
# 아래 코드도 PyPy로만 시간 초과가 안나고 겨우 풀린다.
# 만약 파이썬으로 빠르게 풀고 싶으면 DP로 접근하여 이 문제를 풀어여할 듯 하다
## 나중에 다시 접근할 것!


def move_pipe(a, b, direction):
    global cnt
    if a == N-1 and b == N-1:
        cnt += 1
        return
    if direction == 0 and b < N-1:
        if board[a][b+1] == 0:
            move_pipe(a, b+1, 0)
        if a < N-1 and board[a+1][b] == 0 and board[a][b+1] == 0 and board[a+1][b+1] == 0:
            move_pipe(a+1, b+1, 2)
    if direction == 1 and a < N-1:
        if board[a+1][b] == 0:
            move_pipe(a+1, b, 1)
        if b < N-1 and board[a+1][b] == 0 and board[a][b+1] == 0 and board[a+1][b+1] == 0:
            move_pipe(a+1, b+1, 2)
    if direction == 2:
        if b < N-1 and board[a][b+1] == 0:
            move_pipe(a, b+1, 0)
        if a < N-1 and board[a+1][b] == 0:
            move_pipe(a+1, b, 1)
        if a < N-1 and b < N-1 and board[a+1][b] == 0 and board[a][b+1] == 0 and board[a+1][b+1] == 0:
            move_pipe(a+1, b+1, 2)


N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 0
move_pipe(0, 1, 0)
print(cnt)