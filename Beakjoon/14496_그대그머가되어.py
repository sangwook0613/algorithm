# 백준 14496 그대, 그머가 되어
## BFS를 통해 풀이
## visited로 계산량을 감소
A, B = map(int, input().split())
N, M = map(int, input().split())
visited = [0]*(N+1)
connections = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    connections[i].append(j)
    connections[j].append(i)

q = [A]
visited[A] = 1
while q:
    x = q.pop(0)
    for i in connections[x]:
        if not visited[i]:
            visited[i] = visited[x] + 1
            q.append(i)

print(visited[B]-1)