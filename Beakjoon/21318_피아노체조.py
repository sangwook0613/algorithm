# 백준 21318 피아노체조
## 누적 합을 활용하여 푸는 간단한 문제
## 계산량을 줄여야 할 때 항상 누적 합과 이분 탐색을 고려해보자!
import sys
input = sys.stdin.readline

N = int(input())
difficulty = list(map(int, input().split()))
minus = [0, 0] # 인덱스를 맞추기 위해 0을 하나 더 추가
# 누적 합 구하기
for i in range(1, N):
    if difficulty[i] < difficulty[i-1]:
        minus.append(1 + minus[i])
    else:
        minus.append(minus[i])

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    print(minus[b] - minus[a])