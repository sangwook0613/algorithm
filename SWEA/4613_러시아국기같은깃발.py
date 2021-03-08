def make_flag(start, depth, total, cnt):
    global min_cost
    if depth == N-2:
        if cnt[1] == 0:
            return
        if total < min_cost:
            min_cost = total
        return
    for i in range(start, 3):
        if cnt[i] >= N-3 and i == 0:
            continue
        cnt[i] += 1
        make_flag(i, depth+1, total+(M-colors[depth][i]), cnt)
        cnt[i] -= 1


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    colors = []
    for i in range(N):
        row = [0, 0, 0]
        for j in range(M):
            if flag[i][j] == 'W':
                row[0] += 1
            elif flag[i][j] == 'B':
                row[1] += 1
            else:
                row[2] += 1
        colors += [row]

    ans = 0
    ans += (M*2 - (colors[0][0] + colors[N-1][2]))
    colors = colors[1:N-1]

    min_cost = 10000000
    make_flag(0, 0, 0, [0, 0, 0])
    print('#%d %d' % (t, min_cost+ans))