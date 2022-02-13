# 백준 2725 보이는 점의 개수
## 유클리드 호제법을 활용하여 최대공약수가 1이면 count 하는 문제
### 유클리드 호제법이 아니라 소수를 구하는 패턴으로 착각하여 헤맨 문제
## DP 와 같은 방식으로 미리 1000개를 모두 구해놓는 방식
### DP 를 진행할때 새로운 라인만 count 하여 더해가면 되기에 누적합의 원리를 따른다.
def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


dp = [0]*1001
dp[1] = 3
for i in range(2, 1001):
    cnt = 0
    for j in range(1, i):
        if gcd(i, j) == 1:
            cnt += 1
    dp[i] = dp[i-1] + cnt*2

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])