## 풀이1
def solve(lev, total):
    if memo[lev][total]:
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
memo = [[0 for _ in range(80001)] for __ in range(N + 1)]

solve(0, 0)

ans = []
for i in chk_weight:
    if memo[N][i]:
        ans.append('Y')
    else:
        ans.append('N')

print(' '.join(ans))


## 풀이2
def solve(lev, left, right):
    total = abs(left - right)
    if memo[lev][total]:
        return
    memo[lev][total] = 1
    if lev == N:
        return

    solve(lev + 1, left + weight[lev], right)
    solve(lev + 1, left, right + weight[lev])
    solve(lev + 1, left, right)


N = int(input())
weight = list(map(int, input().split()))

C = int(input())
chk_weight = list(map(int, input().split()))
memo = [[0 for _ in range(40001)] for __ in range(N + 1)]

solve(0, 0, 0)

ans = []
for i in chk_weight:
    if memo[N][i]:
        ans.append('Y')
    else:
        ans.append('N')

print(' '.join(ans))