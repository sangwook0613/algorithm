def init(start, end, node):
    if start == end:
        tree[node] = [numbers[start-1], numbers[start-1]]
        return tree[node]
    mid = (start + end) // 2
    first = init(start, mid, node*2)
    second = init(mid+1, end, node*2 + 1)
    tree[node] = [min(first[0], second[0]), max(first[1], second[1])]
    return tree[node]

def get_minmax(start, end, node, left, right):
    if left > end or right < start:
        return [1000000000, 1]
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    first = get_minmax(start, mid, node*2, left, right)
    second = get_minmax(mid+1, end, node*2 + 1, left, right)
    return [min(first[0], second[0]), max(first[1], second[1])]


N, M = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
tree = [[] for _ in range(N*4)]
init(1, N, 1)

for _ in range(M):
    a, b = map(int, input().split())
    ans = get_minmax(1, N, 1, a, b)
    print(ans[0], ans[1])