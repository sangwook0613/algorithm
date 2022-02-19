# 백준 2167 2차원 배열의 합
## 누적합으로 구하는 문제
## 누적합을 구했으면 어떻게 정답을 도출하는지에 대해서 너무 예민하지 못했다...
N, M = map(int, input().split())
numbers = [[0]*(M+1)]
for _ in range(N):
    numbers.append([0] + list(map(int, input().split())))

K = int(input())
dp = [[0]*(M+1) for _ in range(N+1)]
for a in range(1, N+1):
    for b in range(1, M+1):
        dp[a][b] = dp[a-1][b] + dp[a][b-1] - dp[a-1][b-1] + numbers[a][b]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    ans = dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]
    print(ans)