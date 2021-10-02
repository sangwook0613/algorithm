# 프로그래머스 게임 맵 최단거리
## BFS 문제

from collections import deque

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def solution(maps):
    answer = 0
    row = len(maps)
    col = len(maps[0])
    visited = [[0] * col for _ in range(row)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        a, b = q.popleft()
        for dx, dy in dxy:
            x = a + dx
            y = b + dy
            if 0 <= x < row and 0 <= y < col and not visited[x][y] and maps[x][y]:
                visited[x][y] = visited[a][b] + 1
                q.append((x, y))

    if visited[row - 1][col - 1] == 0:
        return -1
    return visited[row - 1][col - 1]