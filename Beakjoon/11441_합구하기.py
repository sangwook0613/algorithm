# 백준 11441 합 구하기
## 간단한 누적 합 문제
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
total = [0]
for i in range(N):
    total.append(total[i] + numbers[i])

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(total[b] - total[a] + numbers[a-1])