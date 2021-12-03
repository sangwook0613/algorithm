# 백준 2156 포도주 시식
# DP 로 풀어낸 문제
# 연속해서 먹은 횟수에 따라 배열을 나누어 MAX 값을 계산
N = int(input())
wine = [int(input()) for _ in range(N)]
dp = [[0]*3 for _ in range(N)]
dp[0][1] = wine[0]

for i in range(1, N):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] = max(wine[i], dp[i-1][0]+wine[i])
    dp[i][2] = dp[i-1][1] + wine[i]

print(max(dp[N-1]))