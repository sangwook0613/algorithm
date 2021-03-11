# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def print_for(arr):
    for n in range(N):
        print(arr[n])
    print()

def get_max(arr):
    max_num = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_num:
                max_num = arr[i][j]
    return max_num


def dfs(a, b, d, cnt, visited):
    global ans
    if cnt > ans:
        ans = cnt
    # print(a, b, cnt, d)
    # print_for(visited)
    visited[a][b] = 1
    for k in range(4):
        nx = a + dx[k]
        ny = b + dy[k]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if not visited[nx][ny]:
            if mountain[nx][ny] < mountain[a][b]:
                visited[nx][ny] = 1
                dfs(nx, ny, d, cnt+1, visited)
                visited[nx][ny] = 0
            if mountain[nx][ny] >= mountain[a][b] and d != 0 and (mountain[nx][ny] - mountain[a][b]) <= d-1 :
                d = 0
                visited[nx][ny] = 1
                mountain[nx][ny] -= 1
                dfs(nx, ny, d, cnt + 1, visited)
                mountain[nx][ny] += 1
                visited[nx][ny] = 0

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    chk = [[0]*N for _ in range(N)]
    max_height = get_max(mountain)
    ans = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_height:
                # print(i, j)
                dfs(i, j, K, 0, chk)
                chk[i][j] = 0
                # print(ans)

    print(ans+1)
