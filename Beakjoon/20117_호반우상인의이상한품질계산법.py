# 백준 20117 호반우 상인의 이상한 품질 계산법
## 그리디하게 푸는 문제
## 양 끝의 숫자를 하나씩 묶어 항상 + 만 얻을 수 있도록 접근
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
total = 0
# 홀수인 경우
if N % 2:
    total += numbers[N//2]
    for i in range(N-1, N//2,-1):
        total += 2*numbers[i]
# 짝수인 경우
else:
    for i in range(N-1, N//2 -1, -1):
        total += 2*numbers[i]

print(total)