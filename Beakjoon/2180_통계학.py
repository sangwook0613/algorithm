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
        for b in range(i, len(left)):
            result += [left[b]]
    return result


N = int(sys.stdin.readline())
total = 0
numbers = [0] * N
for i in range(N):
    numbers[i] = int(sys.stdin.readline())
    total += numbers[i]

numbers = merge_sort(numbers)

avg = round(total / N)
median = numbers[N // 2]
minmax = numbers[N-1] - numbers[0]


counts = [0] * 8001
for i in range(N):
    counts[numbers[i]+4000] += 1

max_count = 0
for i in range(8001):
    if counts[i] > max_count:
        max_count = counts[i]

mode_list = []
for i in range(8001):
    if counts[i] == max_count:
        mode_list += [i-4000]

mode = 0
if len(mode_list) > 1:
    mode = mode_list[1]
else:
    mode = mode_list[0]

print(avg)
print(median)
print(mode)
print(minmax)