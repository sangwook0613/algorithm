# 백준 17626 Four Squares
## DP 를 활용해서 풀이
### 현재 값도 작은 제곱값을 뺀 수의 개수 + 1로 순차적으로 구함
## 사실 문제를 더 꼼꼼히 읽으면 쉽게 풀 수 있는 문제
## 최대 4개 안에 구할 수 있다고 처리했기 때문에 완전 탐색으로 풀이 가능
N = int(input())
dp = [0, 1]

for i in range(2, N+1):
    temp = 50000
    k = 1

    while k**2 <= i:
        temp = min(temp, dp[i-k**2] + 1)
        k += 1
    dp.append(temp)

print(dp[N])