# 프로그래머스 거리두기 확인하기
## 간단한 bfs 문제

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(a, b, board):
    q = [(a, b, 0)]
    visited = [[0] * 5 for _ in range(5)]
    visited[a][b] = 1

    while q:
        x, y, cost = q.pop(0)
        for dx, dy in dxy:
            r = x + dx
            c = y + dy
            if 0 <= r < 5 and 0 <= c < 5 and not visited[r][c]:
                if board[r][c] == 'P':
                    if cost <= 1:
                        return 0
                elif board[r][c] == 'O':
                    visited[r][c] = 1
                    q.append((r, c, cost + 1))
    return 1


def solution(places):
    answer = []
    for place in places:
        points = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    points.append((i, j))
        total = 0
        for p1, p2 in points:
            total += bfs(p1, p2, place)

        if total == len(points):
            answer.append(1)
        else:
            answer.append(0)
    return answer