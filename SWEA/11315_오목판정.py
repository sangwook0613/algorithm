def check_col(a, b, n):
    chk = 0
    for i in range(1, n+1):
        if board[a+i][b]:
            chk += 1
        else:
            if chk >= 5:
                return 1
            chk = 0
    if chk >= 5:
        return 1
    return 0


def check_row(a, b, n):
    chk = 0
    for i in range(1, n+1):
        if board[a][b+i]:
            chk += 1
        else:
            if chk >= 5:
                return 1
            chk = 0
    if chk >= 5:
        return 1
    return 0


def check_diag1(a, b, n):
    chk = 0
    for i in range(1, n+1):
        if board[a+i][b+i]:
            chk += 1
        else:
            if chk >= 5:
                return 1
            chk = 0
    if chk >= 5:
        return 1
    return 0


def check_diag2(a, b, n):
    chk = 0
    for i in range(1, n+1):
        if board[a-i][b+i]:
            chk += 1
        else:
            if chk >= 5:
                return 1
            chk = 0
    if chk >= 5:
        return 1
    return 0


T = int(input())

for t in range(1, T+1):
    N = int(input())
    board = []
    board += [[0]*(N+2)]
    for n in range(N):
        temp = input()
        board += [[0]]
        for i in range(N):
            if temp[i] == '.':
                board[n+1] += [0]
            else:
                board[n+1] += [1]
        board[n+1] += [0]

    cnt = 1
    if check_diag1(0, 0, N) or check_diag2(N+1, 0, N):
        print('#%d %s' % (t, 'YES'))
        continue

    for i in range(1, N+1):
        if check_row(i, 0, N) or check_col(0, i, N):
            print('#%d %s' % (t, 'YES'))
            cnt = 0
            break
        if N-i >= 5:
            if check_diag1(i, 0, N-i) or check_diag1(0, i, N-i) or check_diag2(N+1, i, N-i):
                print('#%d %s' % (t, 'YES'))
                cnt = 0
                break
        if i >= 6:
            if check_diag2(0, i, i - 1):
                print('#%d %s' % (t, 'YES'))
                cnt = 0
                break
    if cnt:
        print('#%d %s' % (t, 'NO'))