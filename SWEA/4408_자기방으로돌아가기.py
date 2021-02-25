T = int(input())

for t in range(1, T + 1):
    N = int(input())
    rooms = [0] * 201
    for i in range(N):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start
        for i in range((start + 1) // 2, ((end + 1) // 2) + 1):
            rooms[i] += 1

    ans = 0
    for i in rooms:
        if i > ans:
            ans = i
    print('#%d %d' % (t, ans))