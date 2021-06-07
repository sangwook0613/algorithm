tree = [[[], 0, 0, 0]] * 10 * 4


def init(start, end, node, gems, gems_dict):
    if start == end:
        idx = gems_dict[gems[start - 1]]
        temp = [0] * len(gems_dict)
        temp[idx] = 1
        tree[node] = [temp, 0, start, end]
        return tree[node]
    mid = (start + end) // 2
    left = init(start, mid, node * 2, gems, gems_dict)
    right = init(mid + 1, end, node * 2 + 1, gems, gems_dict)
    total = [0] * len(gems_dict)
    chk = 0
    for i in range(len(gems_dict)):
        if left[0][i] or right[0][i]:
            total[i] = left[0][i] + right[0][i]
            chk += 1
    sum_up = [total, 0, start, end]
    if chk == len(gems_dict):
        sum_up[1] = 1
    tree[node] = sum_up
    return tree[node]


def solution(gems):
    gems_set = set(gems)
    gems_dict = {}
    cnt = 0
    for i in gems_set:
        gems_dict[i] = cnt
        cnt += 1
    answer = []
    init(1, len(gems), 1, gems, gems_dict)
    for i in range(len(tree)):
        if tree[i][1]:
            print(tree[i][2], tree[i][3])
    print(tree)
    # print(ans)
    return answer