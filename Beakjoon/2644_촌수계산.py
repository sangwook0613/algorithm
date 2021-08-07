# 2644 촌수계산
## BFS 문제
## 부모와 자식의 연결 처리를 어떻게 보는지가 핵심


def bfs(start, fin):
    q = [(start, 0)]
    visited[start] = 1
    while q:
        x, cnt = q.pop(0)
        for i in connection[x]:
            if i == fin:
                return cnt + 1
            if not visited[i]:
                q.append((i, cnt+1))
                visited[i] = 1
    return -1


N = int(input())
a, b = map(int, input().split())
k = int(input())
total = [0]*(N+1)
connection = [[] for _ in range(N+1)]

for _ in range(k):
    p, c = map(int, input().split())
    connection[c].append(p)
    connection[p].append(c)

visited = [0]*(N+1)
print(bfs(a, b))