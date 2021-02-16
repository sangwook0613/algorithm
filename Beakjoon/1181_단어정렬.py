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
    len_left = len(left)
    len_right = len(right)
    while i < len_left and j < len_right:
        if len(left[i]) > len(right[j]):
            result += [right[j]]
            j += 1
        elif len(left[i]) < len(right[j]):
            result += [left[i]]
            i += 1
        else:
            if left[i] > right[j]:
                result += [right[j]]
                j += 1
            else:
                result += [left[i]]
                i += 1
    if i == len_left:
        for a in range(j, len_right):
            result += [right[a]]
    else:
        for a in range(i, len_left):
            result += [left[a]]
    return result


N = int(input())

words = [input() for n in range(N)]
words = merge_sort(words)

print(words[0])
for i in range(1, N):
    if words[i] != words[i-1]:
        print(words[i])