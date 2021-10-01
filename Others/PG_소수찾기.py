# 프로그래머스 소수찾기
## 부분집합과 순열 문제

from itertools import permutations

def getNum(a):
    result = [1] * (a + 1)
    result[0] = 0
    result[1] = 0
    k = 2
    while k <= a:
        if result[k]:
            for i in range(k * 2, a + 1, k):
                result[i] = 0
        k += 1
    return result


def solution(numbers):
    answer = 0
    nums = [n for n in numbers]
    nums.sort(reverse=True)
    temp_max = ''
    for n in nums:
        temp_max += n
    max_num = int(temp_max)
    chk = getNum(max_num)

    for i in range(1, len(numbers) + 1):
        orders = list(permutations(nums, i))
        for order in orders:
            temp = ''
            for o in order:
                temp += o
            if chk[int(temp)] > 0:
                answer += 1
                chk[int(temp)] = -1

    return answer