# 1806 부분합
## 부분합 or 두 포인터를 다루는 방식으로 풀 수 있는 문제
## 큰 값을 잡을꺼면 애매하게 두지말고 아예 큰 값으로 설정하여 풀자!


N, S = map(int, input().split())
numbers = list(map(int, input().split()))
total = 0
start = end = 0
ans = 100001

for start in range(N):
    while total <= S and end < N:
        total += numbers[end]
        end += 1
    if total >= S:
        ans = min(ans, end - start)
    total -= numbers[start]

if ans == 100001:
    print(0)
else:
    print(ans)