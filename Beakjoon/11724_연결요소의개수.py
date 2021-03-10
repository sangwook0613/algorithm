from collections import deque

def bfs(start, cnt):
    queue = deque()
    queue.append(start)
    visited[start] = cnt
    while queue:
        a = queue.popleft()
        for b in range(len(node[a])):
            if not visited[node[a][b]]:
                visited[node[a][b]] = cnt
                queue.append(node[a][b])


N, M = map(int, input().split())

node = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)

ans = 0
for i in range(1, N+1):
    if not visited[i]:
        ans += 1
        bfs(i, ans)

print(ans)