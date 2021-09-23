# 15486 퇴사 2
## 그리디와 DP를 섞은 문제

import sys

N = int(sys.stdin.readline())
days = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
total = [0]*(N+1)

for i in range(N):
    finish_day = i + days[i][0]
    if finish_day <= N:
        total[finish_day] = max(total[finish_day], total[i] + days[i][1])
    total[i + 1] = max(total[i + 1], total[i])

print(max(total))