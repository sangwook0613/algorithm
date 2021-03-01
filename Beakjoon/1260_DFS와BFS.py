from collections import deque


def DFS(visited, start, ans):
    visited[start] = 1
    ans += [start]
    for i in range(len(connection[start])):
        if not visited[connection[start][i]]:
            DFS(visited, connection[start][i], ans)
    return ans


def BFS(visited, start, ans):
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        ans += [v]
        for i in connection[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
    return ans

N, M, V = map(int, input().split())
connection = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    connection[a] += [b]
    connection[b] += [a]
for i in range(N+1):
    connection[i].sort()

dfs_ans = DFS([0]*(N+1), V, [])
bfs_ans = BFS([0]*(N+1), V, [])

for i in range(len(dfs_ans)):
    print(dfs_ans[i], end=' ')
print()
for i in range(len(bfs_ans)):
    print(bfs_ans[i], end=' ')