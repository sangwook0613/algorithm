# 백준 20152 Game Addiction
## 일종의 DP 같은 문제
## 해당 좌표까지 올 수 있는 경우를 계속 더해가며 목적지까지 도달하는 방식
H, N = map(int, input().split())
D = abs(H-N)
board = [[1] + [0]*D for _ in range(D+1)]

for i in range(1, D+1):
    for j in range(1, D+1):
        if i >= j:
            board[i][j] = board[i][j-1] + board[i-1][j]

print(board[D][D])