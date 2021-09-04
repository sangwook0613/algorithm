# 프로그래머스 H-index
## 문제를 제대로 이해하는데 어려웠던 문제

## 내 풀이
## 정렬 후 이분탐색을 통해 일일이 비교히며 찾았다.
def solution(citations):
    answer = 0
    total = max(citations)
    citations.sort()

    for i in range(total):
        left = 0
        right = len(citations)
        while left <= right:
            mid = (left + right) // 2
            if i > citations[mid]:
                left = mid + 1
            else:
                right = mid - 1

        if right+1 <= i <= len(citations) - left:
            answer = max(answer, i)

    return answer

# 참고 풀이
## 문제를 제대로 이해하지 못한 상태에서는 이분탐색을 통해 하나하나 비교했지만
## 문제를 제대로 이해했다면, 최대값을 구하는 것이기에 내림차순으로 정렬하여 count를 하면 된다..
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    total = len(citations)

    while True:
        count = 0
        for c in citations:
            if c >= total:
                count += 1
            if count >= total:
                return total
        total -= 1