import sys

def init(start, end, node):
    if start == end:
        tree[node] = numbers[start - 1]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(init(start, mid, node*2), init(mid+1, end, node*2 + 1))
    return tree[node]


def get_min(start, end, node, left, right):
    if left > end or right < start:
        return 1000000000
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return min(get_min(start, mid, node*2, left, right), get_min(mid+1, end, node*2 +1, left, right))


N, M = map(int, sys.stdin.readline().split())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
tree = [0]*N*4
init(1, N, 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(get_min(1, N, 1, a, b))