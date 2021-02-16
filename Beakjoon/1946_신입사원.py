## 정렬 하지말고 그대로 리스트로 받아서 풀기 # 이 방법이 더 좋다!
import sys

T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    grade = [0] * (N+1)
    for n in range(N):
        a, b = map(int, sys.stdin.readline().split())
        grade[a] = b

    idx = 1
    cnt = 1
    for i in range(2, N+1):
        if grade[idx] > grade[i]:
            idx = i
            cnt += 1

    print(cnt)


## 분할정렬 활용해서 풀기 ##
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
    if i == len_left:
        for a in range(j, len_right):
            result += [right[a]]
    else:
        for a in range(i, len_left):
            result += [left[a]]
    return result


T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    # list comprehension 을 활용하여 input 받기
    grade = [list(map(int, sys.stdin.readline().split())) for n in range(N)]

    # merge sort 로 정렬
    grade = merge_sort(grade)
    # 상위 지원자보다 높은 등수가 있다면 바꾸기
    idx = 0
    cnt = 1
    for i in range(N):
        if grade[idx][1] > grade[i][1]:
            idx = i
            cnt += 1

    print(cnt)