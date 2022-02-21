# 백준 12015 가장 긴 증가하는 부분 수열2
## 최장 길이 부분 수열 알고리즘을 사용하는 문제
## 단, 입력이 100만까지 들어오기에 nlogn 으로 풀어야하며, 이를 위해 이분탐색을 사용
def binary_search(k):
    left = 0
    right = len(order) - 1
    while left <= right:
        mid = (left + right) // 2
        if order[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return left


N = int(input())
numbers = [0] + list(map(int, input().split()))
dp = [0]*(N+1)
order = [0] # 이분탐색의 대상이 되는 배열

for i in range(1, N+1):
    temp = binary_search(numbers[i])
    if temp >= len(order):
        order.append(numbers[i])
    else:
        # 갱신을 꼭해야한다! 왜?
        ## 최대한 작은 수를 배열에 정리하여 유지하기 위함
        order[temp] = numbers[i]
    dp[i] = temp

print(max(dp))