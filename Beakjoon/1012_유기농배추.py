def dfs(a, b):
    if a < 0 or a > N-1 or b < 0 or b > M-1:
        return False
    if farm[a][b] == 1:
        farm[a][b] = 0
        dfs(a-1, b) # 상
        dfs(a+1, b) # 하
        dfs(a, b-1) # 좌
        dfs(a, b+1) # 우
        return True
    return False


T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())
    farm = [[0]*M for _ in range(N)]
    for k in range(K):
        y, x = map(int, input().split())
        farm[x][y] = 1

    ans = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                ans += 1

    print(ans)