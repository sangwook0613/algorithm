# 백준 5567 결혼식
## 친구의 친구만 찾을 수 있으면 쉽게 풀리는 문제
## 상근이의 친구들과 친구인 번호만 배열에 담아서 확인
N = int(input())
M = int(input())
order = [list(map(int, input().split())) for _ in range(M)]
order.sort(key=lambda x: x[0])
relationship = [[] for _ in range(N+1)]
bestfriend = [0]*(N+1)
bestfriend[1] = 1
for a, b in order:
    if a == 1:
        bestfriend[b] = 1
        continue
    # 상근이의 친구들과 친구인 번호만 배열에 담는다
    if bestfriend[b]:
        relationship[a].append(b)
    if bestfriend[a]:
        relationship[b].append(a)

ans = 0
for i in range(2, N+1):
    if bestfriend[i]:
        ans += 1
    else:
        for k in relationship[i]:
            # 상근이의 친구들과 친구인지 확인 후 count
            if bestfriend[k]:
                ans += 1
                break

print(ans)