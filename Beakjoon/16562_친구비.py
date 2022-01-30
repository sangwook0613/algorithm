# 백준 16562 친구비
## 유니온파인든 알고리즘을 활용해서 풀이
## find 알고리즘을 좀 더 단순화 하려고 노력
def find(x):
    if friends[x] != x:
        friends[x] = find(friends[x])
    return friends[x]

def union(x, y):
    a = find(x)
    b = find(y)
    if a > b:
        friends[a] = b
    else:
        friends[b] = a


N, M, K = map(int, input().split())
cost = list(map(int, input().split()))
connections = [list(map(int, input().split())) for _ in range(M)]
connections.sort()
friends = [i for i in range(N+1)]
for v, w in connections:
    union(v, w)

# 같은 부모를 갖는 친구들의 번호를 dict로 묶음
group = dict()
for i in range(1, N+1):
    temp = find(i)
    if group.get(temp):
        group[temp].append(cost[i-1])
    else:
        group[temp] = [cost[i-1]]

# 그룹별 최소비용 찾아서 더하기
ans = 0
for arr in group.values():
    ans += min(arr)

if ans > K:
    print('Oh no')
else:
    print(ans)