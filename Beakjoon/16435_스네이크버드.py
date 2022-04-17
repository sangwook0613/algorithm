# 백준 16435 스네이크버드
## 단순한 정렬 문제
N, L = map(int, input().split())
fruits = list(map(int, input().split()))
fruits.sort()

for k in fruits:
    if k > L:
        break
    L += 1

print(L)