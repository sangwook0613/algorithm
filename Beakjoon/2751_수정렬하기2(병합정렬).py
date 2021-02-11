def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    else:
        mid_idx = len(numbers) // 2
        leftNumbers = numbers[:mid_idx]
        rightNumbers = numbers[mid_idx:]
        leftNumbers = merge_sort(leftNumbers)
        rightNumbers = merge_sort(rightNumbers)
        return merge(leftNumbers, rightNumbers)


def merge(leftList, rightList):
    result = []
    i = 0
    j = 0
    while i < len(leftList) and j < len(rightList):
        if leftList[i] > rightList[j]:
            result += [rightList[j]]
            j += 1
        else:
            result += [leftList[i]]
            i += 1
    if i == len(leftList):
        for a in range(j, len(rightList)):
            result += [rightList[a]]
    else:
        for a in range(i, len(leftList)):
            result += [leftList[a]]
    return result


N = int(input())
numbers = [0] * N
for i in range(N):
    numbers[i] = int(input())

ans = merge_sort(numbers)
for i in range(len(ans)):
    print(ans[i])