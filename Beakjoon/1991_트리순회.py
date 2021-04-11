def get_order(node, order_type):
    global answer
    if order_type == 0:
        # 전위순회
        answer += chr(tree[node][0] + ascii_num)
        if tree[node][1] != 0:
            get_order(tree[node][1], order_type)
        if tree[node][2] != 0:
            get_order(tree[node][2], order_type)
    elif order_type == 1:
        # 중위순회
        if tree[node][1] != 0:
            get_order(tree[node][1], order_type)
        answer += chr(tree[node][0] + ascii_num)
        if tree[node][2] != 0:
            get_order(tree[node][2], order_type)
    else:
        # 후위순회
        if tree[node][1] != 0:
            get_order(tree[node][1], order_type)
        if tree[node][2] != 0:
            get_order(tree[node][2], order_type)
        answer += chr(tree[node][0] + ascii_num)

N = int(input())
ascii_num = 65
tree = [[i, 0, 0] for i in range(N)]

for i in range(N):
    v, right, left = input().split()
    if right != '.':
        tree[ord(v)-ascii_num][1] = ord(right)-ascii_num
    if left != '.':
        tree[ord(v) - ascii_num][2] = ord(left) - ascii_num

for k in range(3):
    answer = ''
    get_order(0, k)
    print(answer)