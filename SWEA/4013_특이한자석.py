def move_magnet(a, b):
    if b > 0:
        temp = magnet[a][7]
        for i in range(7, 0, -1):
            magnet[a][i] = magnet[a][i-1]
        magnet[a][0] = temp
    else:
        temp = magnet[a][0]
        for i in range(7):
            magnet[a][i] = magnet[a][i+1]
        magnet[a][7] = temp


T = int(input())

for t in range(1, T+1):
    N = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]
    for n in range(N):
        k, d = map(int, input().split())
        idx1 = k-1
        idx2 = k-1
        chk = [0, 0, 0, 0]
        chk[k-1] = d
        while idx1 + 1 < 4:
            if magnet[idx1][2] + magnet[idx1+1][6] == 1:
                if chk[idx1] < 0:
                    chk[idx1+1] = 1
                else:
                    chk[idx1+1] = -1
            else:
                break
            idx1 += 1
        while idx2 > 0:
            if magnet[idx2][6] + magnet[idx2-1][2] == 1:
                if chk[idx2] < 0:
                    chk[idx2-1] = 1
                else:
                    chk[idx2-1] = -1
            else:
                break
            idx2 -= 1

        for c in range(4):
            if chk[c] != 0:
                move_magnet(c, chk[c])

    pow2 = [1, 2, 4, 8]
    ans = 0
    for j in range(4):
        ans += magnet[j][0] * pow2[j]

    print('#%d %d' % (t, ans))