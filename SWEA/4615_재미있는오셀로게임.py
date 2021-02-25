# 상 하 좌 우 우상 좌상 우하 좌하
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]


def check_board(a, b, color):
    change = []
    idx = 0
    x = a
    y = b
    temp = []
    while idx < 8:
        x += dx[idx]
        y += dy[idx]
        if board[x][y] == 3-color:
            temp += [(x, y)]
            continue
        else:
            if len(temp) > 0 and board[x][y] == color:
                change += temp
            temp = []
            x = a
            y = b
            idx += 1
    for i, j in change:
        board[i][j] = color


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*(N+2) for _ in range(N+2)]
    board[N//2][N//2] = 2
    board[N//2+1][N//2+1] = 2
    board[N//2+1][N//2] = 1
    board[N//2][N//2+1] = 1

    for i in range(M):
        a, b, c = map(int, input().split())
        board[b][a] = c
        check_board(b, a, c)

    black = 0
    white = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print('#%d %d %d' % (t, black, white))