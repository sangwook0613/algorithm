# 백준 1453 피시방 알바
N = int(input())
print(N - len(set(list(map(int, input().split())))))