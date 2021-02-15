import sys


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid_idx = len(arr) // 2
    leftList = merge_sort(arr[:mid_idx])
    rightList = merge_sort(arr[mid_idx:])
    return merge(leftList, rightList)


def merge(left, right):
    result = []
    i = 0
    j = 0
    left_len = len(left)
    right_len = len(right)
    while i < left_len and j < right_len:
        if left[i][1] > right[j][1]:
            result += [right[j]]
            j += 1
        elif left[i][1] < right[j][1]:
            result += [left[i]]
            i += 1
        else:
            if left[i][0] > right[j][0]:
                result += [right[j]]
                j += 1
            else:
                result += [left[i]]
                i += 1
    if i == left_len:
        for a in range(j, right_len):
            result += [right[a]]
    else:
        for a in range(i, left_len):
            result += [left[a]]
    return result


N = int(sys.stdin.readline())
pairs = []

# input 받기
for i in range(N):
    pairs += [list(map(int, sys.stdin.readline().split()))]

pairs = merge_sort(pairs)

for p in range(N):
    print(pairs[p][0], pairs[p][1])