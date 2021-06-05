import sys

def init(start, end, node):
    if start == end:
        tree[node] = numbers[start-1]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2 + 1)
    return tree[node]

def prefix_sum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return prefix_sum(start, mid, node*2, left, right) + prefix_sum(mid+1, end, node*2 + 1, left, right)

def update(start, end, node, idx, diff):
    if idx < start or idx > end:
        return
    tree[node] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node*2, idx, diff)
    update(mid+1, end, node*2 + 1, idx, diff)


N, Q = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
tree = [0]*N*4
init(1, N, 1)

for _ in range(Q):
    s, e, a, b = map(int, sys.stdin.readline().split())
    if s > e:
        print(prefix_sum(1, N, 1, e, s))
    else:
        print(prefix_sum(1, N, 1, s, e))
    change = b - numbers[a-1]
    update(1, N, 1, a, change)
    numbers[a-1] = b