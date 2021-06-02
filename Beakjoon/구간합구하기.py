def init(start, end, node):
    '''
    초기 리스트의 구간합을 계산한 세그먼트 트리를 완성시키는 함수
    start와 end가 같다면 해당 node에 값을 입력하고 이후 위로 올라가면서 더해가는 개념
    start: 세그먼트 트리의 노드 배열에서 시작이 될 인덱스
           이진 트리로 구성하기에 1로 시작한다
    end: 범위의 끝이 될 인덱스, 초기 리스트(numbers)의 length
    node: tree의 노드 인덱스
    '''
    if start == end:
        tree[node] = numbers[start-1] # 1로 시작하기에 1를 빼줘야한다.
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2 + 1)
    return tree[node]


def prefix_sum(start, end, node, left, right):
    '''
    left 와 right 내 구간의 합을 계산하는 함수
    start: 범위의 시작(초기값 = 1)
    end: 범위의 마지막(초기값 = numbers 의 길이)
    node: tree 노드의 인덱스
    left: 구간의 시작 인덱스
    right: 구간의 마지막 인덱스
    '''
    # 해당 구간을 벗어난 경우 0을 반환하여 구간 합에 관여 X
    if left > end or right < start:
        return 0
    # 해당 구간 안이라면 tree[node] 값을 반환해서 더함
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return prefix_sum(start, mid, node*2, left, right) + prefix_sum(mid+1, end, node*2 + 1, left, right)


def update(start, end, node, idx, diff):
    '''
    idx 에 위치한 값을 diff 만큼 바뀐 것을 tree에 반환해주는 함수
    start: 범위의 시작(초기값 = 1)
    end: 범위의 마지막(초기값 = numbers 의 길이)
    node: tree 노드의 인덱스
    idx: 바뀐 값의 인덱스 값
    diff: 기존 값과 바뀐 값의 차이
    '''
    # 해당 범위 내 idx 가 포함되지 않는다면 return
    if idx > end or idx < start:
        return
    # 포함된다면 차이값을 더해준다
    tree[node] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node*2, idx, diff)
    update(mid+1, end, node*2 + 1, idx, diff)


N, M, K = map(int, input().split())
numbers = []
tree = [0]*N*4
for i in range(N):
    numbers.append(int(input()))

init(1, N, 1)
cnt = 0
while cnt < (M + K):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        update(1, N, 1, temp[1], temp[2]-numbers[temp[1]-1])
        # tree 업데이트 이후, 실제 numbers 리스트도 업데이트해준다
        numbers[temp[1]-1] = temp[2]
    if temp[0] == 2:
        print(prefix_sum(1, N, 1, temp[1], temp[2]))
    cnt += 1