# 상 하 좌 우 좌상 우상 좌하 우하
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def find_omok(a, b):
    cnt = 1
    idx = 0
    x = a
    y = b
    while idx < 8:
        x += dx[idx]
        y += dy[idx]
        if board[x][y] == 2:
            cnt += 1
        else:
            if cnt >= 5:
                return 1
            else:
                x = a
                y = b
                cnt = 1
                idx += 1
    return 0

T = int(input())

for t in range(1, T+1):
    N = int(input())
    board_str = [input() for _ in range(N)]
    board = []
    for i in range(N+2):
        if i == 0 or i == N+1:
            board += [[0]*(N+2)]
        else:
            temp = []
            for j in range(N+2):
                if j == 0 or j == N + 1:
                    temp += [0]
                elif board_str[i-1][j-1] == '.':
                    temp += [1]
                else:
                    temp += [2]
            board += [temp]

    chk = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 2:
                chk = find_omok(i, j)
                if chk:
                    break
        if chk:
            break
    if chk:
        print('#%d YES' % t)
    else:
        print('#%d NO' % t)