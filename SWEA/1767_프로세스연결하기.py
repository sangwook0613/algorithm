dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solve(idx, cnt, total):
    global max_cnt, min_total
    if idx == len(core):
        if cnt < max_cnt:
            return
        if cnt > max_cnt:
            max_cnt = cnt
            min_total = total
        if cnt == max_cnt:
            if total < min_total:
                min_total = total
        return

    for i in range(idx, len(core)):
        x, y = core[i]
        for j in range(4):
            temp_cnt = chk_able(x, y, j, 0)
            if temp_cnt > 0:
                pa, pb = paint(x, y, dx[j], dy[j])
                solve(i+1, cnt+1, total+temp_cnt)
                re_paint(pa, pb, dx[(j+2)%4], dy[(j+2)%4])


def chk_able(a, b, d, cnt):
    while True:
        a += dx[d]
        b += dy[d]
        cnt += 1
        if board[a][b] < 0:
            return cnt-1
        if board[a][b] != 0:
            return 0


def paint(a, b, da, db):
    while True:
        a += da
        b += db
        if board[a][b] < 0:
            return a, b
        board[a][b] = 2


def re_paint(a, b, da, db):
    while True:
        a += da
        b += db
        if board[a][b] != 2:
            return
        board[a][b] = 0


T = int(input())

for t in range(1, T+1):
    N = int(input())
    board = [[-1]*(N+2)]
    for _ in range(N):
        temp = [-1]
        temp += list(map(int, input().split()))
        temp += [-1]
        board += [temp]
    board += [[-1]*(N+2)]

    core = []
    for i in range(N+2):
        for j in range(N+2):
            block_cnt = 0
            chk = 1
            if board[i][j] == 1:
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if board[ni][nj] < 0:
                        board[i][j] = 3
                        chk = 0
                        break
                    if board[ni][nj] > 0:
                        block_cnt += 1
                if block_cnt == 4:
                    board[i][j] = 3
                    continue
                if chk:
                    core += [(i, j)]

    max_cnt = 0
    min_total = 10000
    solve(0, 0, 0)
    print('#%d %d' % (t, min_total))