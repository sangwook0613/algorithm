T = int(input())


def get_diff(arr):
    total = []
    for ls in arr:
        temp = 0
        for a in range(len(ls)):
            for b in range(len(ls)):
                temp += table[ls[a]][ls[b]]
        total.append(temp)
    return abs(total[0] - total[1])


def make_group(a, group):
    global ans
    if len(group) == N // 2:
        temp1 = []
        temp2 = []
        temp1.append(group)
        for k in range(N):
            if not chk[k]:
                temp2.append(k)
        temp1.append(temp2)
        diff = get_diff(temp1)
        if diff < ans:
            ans = diff
        return
    for i in range(a+1, N):
        chk[i] = 1
        group.append(i)
        make_group(i, group)
        group.pop()
        chk[i] = 0


for t in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    chk = [0]*N
    ans = 100000
    make_group(0, [])
    print('#%d %d' % (t, ans))