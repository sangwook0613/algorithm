# 백준 13460 구슬 탈출2
N, M = map(int, input().split())
board = [input() for _ in range(N)]
hole = []
red = []
blue = []
for i in range(1, N-1):
    for j in range(1, M-1):
        if board[i][j] == 'B':
            blue = [i, j]
        if board[i][j] == 'R':
            red = [i, j]
        if board[i][j] == 'O':
            hole = [i, j]

print(hole, red, blue)