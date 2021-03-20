dxy = [
    [[(1, 0)], [(-1, 0)], [(0, 1)], [(0, -1)]], # 1
    [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]], # 2
    [[(1, 0), (0, 1)], [(1, 0), (0, -1)], [(-1, 0), (0, 1)], [(-1, 0), (0, -1)]], # 3
    [[(1, 0), (0, 1), (0, -1)], [(1, 0), (-1, 0), (0, -1)], [(1, 0), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (0, -1)]], # 4
    [[(1, 0), (-1, 0), (0, 1), (0, -1)]], # 5
]

def get_sum(arr):
    total = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0 and board[r][c] == 0:
                total += 1
    return total


def chk_space(x, y, direction):
    idx = 0
    nx = x
    ny = y
    while idx != len(direction):
        nx += direction[idx][0]
        ny += direction[idx][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny] == 6:
            idx += 1
            nx = x
            ny = y
        visited[nx][ny] += 1


def erase_space(x, y, direction):
    idx = 0
    nx = x
    ny = y
    while idx != len(direction):
        nx += direction[idx][0]
        ny += direction[idx][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny] == 6:
            idx += 1
            nx = x
            ny = y
        visited[nx][ny] -= 1


def solve(p):
    if p == len(cctv):
        global ans
        cnt = get_sum(visited)
        ans = min(ans, cnt)
        return
    for k in range(len(dxy[cctv[p][2] - 1])):
        chk_space(cctv[p][0], cctv[p][1], dxy[cctv[p][2]-1][k])
        solve(p+1)
        erase_space(cctv[p][0], cctv[p][1], dxy[cctv[p][2]-1][k])


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cctv = []
for i in range(N):
    for j in range(M):
        if board[i][j] != 0 and board[i][j] != 6:
            cctv.append((i, j, board[i][j]))

visited = [[0]*M for _ in range(N)]

ans = 1000
solve(0)
print(ans)