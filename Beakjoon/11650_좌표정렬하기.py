def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid_idx = len(arr) // 2
    leftList = merge_sort(arr[:mid_idx])
    rightList = merge_sort(arr[mid_idx:])
    # print(arr)
    # print(leftList, rightList)
    return merge(leftList, rightList)


def merge(left, right):
    result = []
    i = 0
    j = 0
    if right == None:
        right_len = 0
    if right != None:
        right_len = len(right)
    if left == None:
        left_len = 0
    if left != None:
        left_len = len(left)

    while i < left_len and j < right_len:
        if left[i][0] > right[j][0]:
            result += [right[j]]
            j += 1
        elif left[i][0] < right[j][0]:
            result += [left[i]]
            i += 1
        else:
            if left[i][1] > right[j][1]:
                result += [right[j]]
                j += 1
            else:
                result += [left[i]]
                i += 1
    if i == left_len:
        for a in range(j, len(right)):
            result += [right[a]]
    else:
        for a in range(i, len(left)):
            result += [left[a]]
    return result


N = int(input())
numbers = []

for i in range(N):
    numbers += [list(map(int, input().split()))]

numbers = merge_sort(numbers)
for i in range(len(numbers)):
    print(numbers[i][0], numbers[i][1])