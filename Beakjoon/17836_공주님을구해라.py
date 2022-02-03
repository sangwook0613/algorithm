# 백준 17836 공주님을 구해라!
## BFS로 풀되, 검을 얻으면 최단 거리를 구하는 문제
## 검을 얻는 순간 추가적인 visited 처리를 하는 것이 아닌, 바로 공주까지의 최단거리를 구하면 된다.
import sys
from collections import deque
input = sys.stdin.readline
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(t):
    q = deque([(0, 0)])
    visited[0][0] = 1
    with_sword = 0 # 검을 구했다면, 그 때 최단거리를 담을 변수
    while q:
        a, b = q.popleft()
        if visited[N-1][M-1]:
            # 만약 검을 구했다면, 가장 짧을 걸 찾아서 return
            return min(visited[N-1][M-1], with_sword) if with_sword else visited[N-1][M-1]
        if visited[a][b] > t:
            continue
        for dx, dy in dxy:
            x = a + dx
            y = b + dy
            if 0 <= x < N and 0 <= y < M and not visited[x][y]:
                # 검을 얻은 경우
                if maze[x][y] == 2:
                    visited[x][y] = visited[a][b] + 1
                    # 검을 찾을 때까지 온 거리 + 지금 위치에서 공주까지의 최단 거리
                    with_sword = visited[x][y] + abs(N-1-x) + abs(M-1-y)
                    q.append((x, y))
                # 벽인 경우
                elif maze[x][y] == 1:
                    continue
                else:
                    visited[x][y] = visited[a][b] + 1
                    q.append((x, y))

    return with_sword if 0 < with_sword <= t+1 else 0


N, M, T = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

ans = bfs(T) - 1
print(ans if ans > 0 else 'Fail')