def init(start, end, node):
    if start == end:
        tree[node] = numbers[start-1]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = (init(start, mid, node * 2) * init(mid + 1, end, node * 2 + 1)) % 1000000007
    return tree[node]

def prefix_multi(start, end, node, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return (prefix_multi(start, mid, node*2, left, right) * prefix_multi(mid+1, end, node*2 + 1, left, right)) % 1000000007

def update(start, end, node, idx, val):
    if idx > end or idx < start:
        return
    if start == end:
        tree[node] = val
        return
    mid = (start + end) // 2
    update(start, mid, node*2, idx, val)
    update(mid + 1, end, node*2 + 1, idx, val)
    tree[node] = (tree[node*2] * tree[node*2+1]) % 1000000007


N, M, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
tree = [0]*N*4
init(1, N, 1)

for _ in range(M+K):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        numbers[temp[1]-1] = temp[2]
        update(1, N, 1, temp[1], temp[2])
    else:
        print(prefix_multi(1, N, 1, temp[1], temp[2]))


