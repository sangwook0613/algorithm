# 백준 9934 완전 이진 트리
## 완전 이진 트리를 배열로 관리하여 인덱스를 계산하면서 처리
K = int(input())
order = list(map(int, input().split()))
tree = [0]*2**K

idx = 1
a = 0
while a < 2**K - 1:
    # 잎 노드에 있다면
    if idx*2 >= 2**K:
        tree[idx] = order[a]
        a += 1
        idx //= 2
    else:
        # 현재 노드가 찬 경우 부모로
        if tree[idx]:
            idx //= 2
        else:
            # 왼쪽으로 내려간다
            if not tree[idx*2]:
                idx *= 2
            # 왼쪽으로 못 가면
            else:
                tree[idx] = order[a]
                a += 1
                idx = 2*idx + 1

for k in range(K):
    for j in range(2**k, 2**(k+1)):
        print(tree[j], end=' ')
    print()