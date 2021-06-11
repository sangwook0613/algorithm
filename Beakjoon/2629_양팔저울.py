def solve(lev, total):
    if memo[lev][total] or total > 15000:
        return
    memo[lev][total] = 1
    if lev == N:
        return

    solve(lev + 1, total + weight[lev])
    solve(lev + 1, total)
    solve(lev + 1, total - weight[lev])


N = int(input())
weight = list(map(int, input().split()))

C = int(input())
chk_weight = list(map(int, input().split()))
memo = [[0]*30000 for _ in range(30)]

solve(0, 0)

ans = []
for i in chk_weight:
    if memo[N][i]:
        ans.append('Y')
    else:
        ans.append('N')

print(' '.join(ans))