# 그대로 상 우 하 좌
dxy = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]


T = int(input())


for t in range(1, T+1):
    M, A = map(int, input().split())
    wayA = list(map(int, input().split()))
    wayB = list(map(int, input().split()))
    board = [[[] for _ in range(10)] for _ in range(10)]
    energy = []
    for i in range(A):
        a, b, c, d = map(int, input().split())
        energy.append(d)
        for x in range(-c, c+1, 1):
            for y in range(-c, c+1, 1):
                if abs(x) + abs(y) > c:
                    continue
                dx = b-1+x
                dy = a-1+y
                if dx < 0 or dx >= 10 or dy < 0 or dy >= 10:
                    continue
                board[dx][dy].append(i+1)

    for bor in board:
        print(bor)
    print()

    totalA = 0
    totalB = 0
    if len(board[0][0]) != 0:
        totalA += energy[board[0][0][0]-1]
    if len(board[9][9]) != 0:
        totalB += energy[board[9][9][0]-1]
    print(totalA, totalB)

    ax = 0
    ay = 0
    bx = 9
    by = 9
    for i in range(M):
        ax += dxy[wayA[i]][0]
        ay += dxy[wayA[i]][1]
        bx += dxy[wayB[i]][0]
        by += dxy[wayB[i]][1]
        print(i, ax, ay, bx, by)
        print(board[ax][ay], board[bx][by])
        if len(board[ax][ay]) > 0 and len(board[bx][by]) > 0:

            print('YES!')
        if len(board[ax][ay]) > 0:
            totalA += energy[board[ax][ay][0]-1]
        if len(board[bx][by]) > 0:
            totalB += energy[board[bx][by][0]-1]
        print(totalA, totalB)
