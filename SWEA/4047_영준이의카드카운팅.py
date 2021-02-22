T = int(input())

for t in range(1, T+1):
    cards = input()
    chk = []
    for i in range(4):
        chk += [[False]*13]

    idx = 0
    ans = 0
    while idx < len(cards):
        chk_idx = 0
        if cards[idx] == 'S':
            chk_idx = 0
        elif cards[idx] == 'D':
            chk_idx = 1
        elif cards[idx] == 'H':
            chk_idx = 2
        else:
            chk_idx = 3
        num = int(cards[idx+1:idx+3])
        if chk[chk_idx][num-1]:
            ans = 1
            break
        else:
            chk[chk_idx][num-1] = True
        idx += 3

    if ans:
        print('#%d %s' % (t, 'ERROR'))
    else:
        print('#%d' % t, end=' ')
        for i in range(4):
            cnt = 0
            for j in range(13):
                if chk[i][j]:
                    cnt += 1
            print(13-cnt, end=' ')
        print()