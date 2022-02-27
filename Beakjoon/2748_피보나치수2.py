# 백준 2748 피보나치수 2
## DP
N = int(input())
dp = [0, 1]
for i in range(1, N):
    dp.append(dp[i] + dp[i-1])

print(dp[N])

## 재귀
## 재귀는 O(2^n) 이기에 무조건 시간초과
N = int(input())

def solve(k):
    if k <= 1:
        return k
    return solve(k-1) + solve(k-2)

print(solve(N))

## 반복
N = int(input())
a, b = 0, 1
for _ in range(N):
    a, b = b, a+b
print(a)