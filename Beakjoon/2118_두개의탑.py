# 백준 2118 두 개의 탑
# 누적합을 활용하는 문제
# 누적합을 통해 경우의 수를 줄였으나, 더 작게 줄일 수 있는 방법이 있을 것 같다!
# 스터디를 통해 보완해보자!!
N = int(input())
cost = [int(input()) for _ in range(N)]
acc_cost = [0]*N
acc_cost[0] = cost[0]
for c in range(1, N):
        acc_cost[c] = acc_cost[c-1]+cost[c]

ans = 0
for a in range(N):
    temp = 0
    for b in range(a, a+N//2+1):
        if b >= N:
            b -= N
            temp = acc_cost[b] + acc_cost[N-1] - acc_cost[a] + cost[a]
        else:
            temp = acc_cost[b] - acc_cost[a] + cost[a]
        ans = max(ans, min(temp, acc_cost[N-1]-temp))

print(ans)