def get_order(a):
    global ans
    if a != 0:
        get_order(left[a])
        ans.append(words[a])
        get_order(right[a])


for t in range(1, 11):
    N = int(input())

    ans = []
    tree = [[] for _ in range(N + 1)]
    words = [''] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for n in range(N):
        inputs = list(input().split())
        words[int(inputs[0])] = inputs[1]
        if len(inputs) >= 3:
            left[int(inputs[0])] = int(inputs[2])
        if len(inputs) == 4:
            right[int(inputs[0])] = int(inputs[3])

    get_order(1)
    print('#%d %s' % (t, ''.join(ans)))