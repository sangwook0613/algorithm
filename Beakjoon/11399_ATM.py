def merge(arr):
    if len(arr) == 1:
        return arr
    mid_idx = len(arr) // 2
    left_arr = merge(arr[:mid_idx])
    right_arr = merge(arr[mid_idx:])
    return merge_sort(left_arr, right_arr)


def merge_sort(left, right):
    result = []
    l = 0
    r = 0
    while l != len(left) and r != len(right):
        if left[l] > right[r]:
            result += [right[r]]
            r += 1
        else:
            result += [left[l]]
            l += 1
    if l != len(left):
        for a in range(l, len(left)):
            result += [left[a]]
    else:
        for a in range(r, len(right)):
            result += [right[a]]
    return result


N = int(input())
numbers = list(map(int, input().split()))
numbers = merge(numbers)

total = 0
ans = 0
for num in numbers:
    total += num
    ans += total

print(ans)