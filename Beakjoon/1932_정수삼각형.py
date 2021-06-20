N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

chk = [[0]*N for _ in range(N)]
chk[0][0] = triangle[0][0]
for i in range(N):
    for k in range(i):
        chk[i][k] = max(triangle[i][k] + chk[i-1][k], chk[i][k])
        chk[i][k+1] = max(triangle[i][k+1] + chk[i-1][k], chk[i][k+1])

ans = max(chk[N-1])
print(ans)