def chk_leftover(nh, nw):
    total = 0
    # 인덱스를 받아오기에 짝수인경우
    if nh % 2:
        leftover_height = ((H - nh - 1) // 2)
        total += leftover_height * (W // 2)
    # 홀수인 경우
    else:
        total += (W - nw) // 2
        leftover_height = ((H - nh) // 2) - 1
        total += leftover_height * (W // 2)
    return total


def solve(i, j, cnt):
    global max_cnt
    if j > W-1:
        i += 1
        j = 0
    if i == H - 1:
        max_cnt = max(max_cnt, cnt)
        return

    if i+1 < H and j+1 < W and wafer[i][j] == 0 and wafer[i+1][j] == 0 and wafer[i][j+1] == 0 and wafer[i+1][j+1] == 0:
        if chk_leftover(i, j) + cnt <= max_cnt:
            return
        for a in range(i, i + 2):
            for b in range(j, j + 2):
                wafer[a][b] = 2
        solve(i, j+2, cnt + 1)
        for a in range(i, i + 2):
            for b in range(j, j + 2):
                wafer[a][b] = 0

    solve(i, j + 1, cnt)


T = int(input())

for t in range(1, T + 1):
    H, W = map(int, input().split())
    wafer = [list(map(int, input().split())) for _ in range(H)]
    max_cnt = stop = 0
    solve(0, 0, 0)
    print('#%d %d' % (t, max_cnt))