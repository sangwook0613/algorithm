# 백준 6236 용돈 관리
## 이분탐색을 활용해서 풀어야하는 문제
## 처음에는 이분 탐색에 들어갈 left, right를 반복문을 돌면서 구해주려 했으나, python3에서 시간초과
## 이분 탐색으로 모든 경우를 고려하기에 left, right를 굳이 찾아줄 필요가 없다는 것을 판단
import sys
input = sys.stdin.readline

def get_count(cash):
    # 최소 몇번 인출해야하는지 확인
    curr = cash
    cnt = 1
    for d in days:
        # 이미 M보다 크다면 return
        if cnt > M:
            return cnt
        if curr < d:
            curr = cash - d
            cnt += 1
        else:
            curr -= d
    return cnt


def binary_search(left, right):
    while left <= right:
        mid = (left + right) // 2
        temp = get_count(mid)
        # M보다 작거나 같으면, 더 작은 인출 금액을 찾아본다
        if temp <= M:
            right = mid - 1
        else:
            left = mid + 1
    return left


N, M = map(int, input().split())
days = [int(input()) for _ in range(N)]
money = sum(days) + 1 # 최댓값
# 이분 탐색을 시작할 때, 최솟값은 사용할 금액 중 max 값을, 최댓값 모든 인출금액 합친거 + 1로 진행
print(binary_search(max(days), money))