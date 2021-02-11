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
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result += [left[i]]
            i += 1
        else:
            result += [right[j]]
            j += 1
    if i == len(left):
        for a in range(j, len(right)):
            result += [right[a]]
    else:
        for a in range(i, len(left)):
            result += [left[a]]
    return result


number = input()
numbers = []
for i in range(len(number)):
    numbers += [int(number[i])]

numbers = merge_sort(numbers)
ans = ''
for i in range(len(numbers)):
    ans += str(numbers[i])
print(ans)