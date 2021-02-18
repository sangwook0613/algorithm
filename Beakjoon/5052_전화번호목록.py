def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid_idx = len(arr) // 2
    leftList = merge_sort(arr[:mid_idx])
    rightList = merge_sort(arr[mid_idx:])
    return merge(leftList, rightList)


def merge(left, right):
    result = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if int(left[l]) > int(right[r]):
            result += [right[r]]
            r += 1
        else:
            result += [left[l]]
            l += 1
    if l == len(left):
        for a in range(r, len(right)):
            result += [right[a]]
    else:
        for a in range(l, len(left)):
            result += [left[a]]
    return result


T = int(input())

for t in range(T):
    N = int(input())
    num = [input() for _ in range(N)]
    numbers = []
    for i in range(10):
        numbers += [[]]

    for i in range(N):
        numbers[int(num[i][0])] += [num[i]]

    chk = 0
    for i in range(10):
        if len(numbers[i]) > 1:
            numbers[i] = merge_sort(numbers[i])
            for a in range(len(numbers[i])-1):
                word = numbers[i][a]
                for b in range(a+1, len(numbers[i])):
                    if word == numbers[i][b][:len(word)]:
                        chk = 1
                        break
                if chk:
                    break
        if chk:
            break

    if chk:
        print('NO')
    else:
        print('YES')