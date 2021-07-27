# 11404 플로이드
## 플로이드 마샬 알고리즘에 대한 이해가 필요한 문제
## 큰 값은 그냥 터무니 없이 큰 값으로 잡자!


BIG = 10000000
N = int(input())
M = int(input())
board = [[BIG]*N for _ in range(N)]
for _ in range(M):
    s, e, c = map(int, input().split())
    board[s-1][e-1] = min(board[s-1][e-1], c)

# 플로이드 마샬 알고리즘
for k in range(N):
    board[k][k] = 0
    for i in range(N):
        for j in range(N):
            board[i][j] = min(board[i][j], board[i][k]+board[k][j])

for a in range(N):
    for b in range(N):
        if board[a][b] == BIG:
            board[a][b] = 0
        print(board[a][b], end=' ')
    print()