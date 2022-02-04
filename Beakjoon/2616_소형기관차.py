# 백준 2616 소형기관차
## 연속적인 것을 고려하여 처리하기 위해 DP 로 풀이
### DP를 통해 해당 지점까지 기관차가 1, 2, 3개인 경우의 최대값을 갱신하면서 진행
## 연속 합을 구하기 위해서는 구간 합을 활용
N = int(input())
numbers = [0] + list(map(int, input().split()))
K = int(input())

# 구간 합 활용
total = [0]
for i in range(1, N+1):
    total.append(numbers[i]+total[i-1])
blocks = []
for i in range(K, N+1):
    blocks.append(total[i] - total[i-K])

# DP
dp = [[0]*(len(blocks)) for _ in range(3)]
dp[0][0] = blocks[0]
for i in range(1, len(blocks)):
    # 2K 이상인 경우부터는 3개 기관차인 경우 고려 가능
    if i >= 2*K:
        dp[1][i] = max(blocks[i] + dp[0][i-K], dp[1][i-1])
        dp[2][i] = max(blocks[i] + dp[1][i-K], dp[2][i-1])
    # K 이상인 경우부터는 2개 기관차인 경우 고려 가능
    elif i >= K:
        dp[1][i] = max(blocks[i] + dp[0][i-K], dp[1][i-1])
    # 기본적으로 1개 기관차인 경우는 계속해서 고려하여 값을 갱신한다.
    dp[0][i] = max(blocks[i], dp[0][i-1])

print(dp[2][len(blocks)-1])