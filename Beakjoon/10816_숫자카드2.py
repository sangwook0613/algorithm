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
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result += [right[j]]
            j += 1
        else:
            result += [left[i]]
            i += 1
    if i == len(left):
        for a in range(j, len(right)):
            result += [right[a]]
    else:
        for a in range(i, len(left)):
            result += [left[a]]
    return result

def binary_search(arr, num, start, end):
    if start > end:
        return 0
    mid_idx = (start + end) // 2
    if arr[mid_idx] == num:
        return 1
    elif arr[mid_idx] > num:
        return binary_search(arr, num, start, mid_idx-1)
    else:
        return binary_search(arr, num, mid_idx + 1, end)


N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

save_idx = [0] * 20000001

check_sorted = merge_sort(check)

for i in range(N):
    if binary_search(check_sorted, numbers[i], 0, M-1):
        save_idx[numbers[i]+10000000] += 1

for i in range(M):
    print(save_idx[check[i]+10000000], end=' ')