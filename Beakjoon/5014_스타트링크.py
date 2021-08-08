# 5014 스타트링크
## 간단한 BFS 문제


def bfs(s):
    q = [(s, 0)]
    visited[s] = 1
    while q:
        current, cnt = q.pop(0)
        if current == end:
            return cnt
        going_up = current + up
        going_down = current - down
        if going_up <= F and not visited[going_up]:
            visited[going_up] = 1
            q.append((going_up, cnt+1))
        if going_down > 0 and not visited[going_down]:
            visited[going_down] = 1
            q.append((going_down, cnt+1))
    return 'use the stairs'


F, start, end, up, down = map(int, input().split())
visited = [0]*(F+1)
print(bfs(start))