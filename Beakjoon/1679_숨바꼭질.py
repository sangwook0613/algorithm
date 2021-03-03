from collections import deque


def solve(a):
    queue = deque([a])
    while queue:
        x = queue.popleft()
        if road[K] != 0:
            break
        if (x - 1) >= 0 and road[x-1] == 0:
            queue.append(x-1)
            road[x-1] = road[x] + 1
        if (x + 1) <= 100000 and road[x+1] == 0:
            queue.append(x+1)
            road[x+1] = road[x] + 1
        if (2 * x) <= 100000 and road[2*x] == 0:
            queue.append(2*x)
            road[2*x] = road[x] + 1
    return road[K]


N, K = map(int, input().split())
road = [0]*100001
if N == K:
    print(0)
else:
    print(solve(N))