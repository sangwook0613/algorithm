# 11048 이동하기
## BFS 인줄 알았으나 3의 1000제곱이기에 시간초과가 난다
## DP로 다시 풀어보자

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = board[i-1][j-1] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[N][M])