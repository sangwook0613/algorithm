# 백준 2294 동전 2
## DP 문제
## 모든 경우를 다 흝어보는지를 항상 확인해야한다!
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort()
dp = [0]*(K+1)

# 1부터 K까지 모두 본다!
for i in range(1, K+1):
    dp[i] = 1000000
    for c in coins:
        # i가 현재 C보다 크다면, i-c 값이 있는지 확인!
        # dp[i-c] 가 1000000 이면 없는 뜻이니 무시
        if i >= c:
            dp[i] = min(dp[i], dp[i-c]+1)
        else:
            break

print(dp[K] if dp[K] != 1000000 else -1)