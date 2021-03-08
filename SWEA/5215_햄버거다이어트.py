def best_comb(a, total, kcal):
    global max_taste
    if total > max_taste:
        max_taste = total
    for i in range(a, N):
        if kcal+cals[i] > L:
            continue
        if total+expect[i] <= max_taste:
            break
        best_comb(i+1, total+points[i], kcal+cals[i])


T = int(input())

for t in range(1, T+1):
    N, L = map(int, input().split())
    points = []
    cals = []
    for i in range(N):
        p, c = map(int, input().split())
        points += [p]
        cals += [c]

    expect = [0] * N
    expect[N-1] = points[N-1]
    for x in range(N-2, -1, -1):
        expect[x] = expect[x+1] + points[x]

    max_taste = 0
    best_comb(0, 0, 0)
    print('#%d %d' % (t, max_taste))