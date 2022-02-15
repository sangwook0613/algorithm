# 백준 11586 민균이의 계략
# O(n2) 풀이
N = int(input())
numbers = list(map(int, input().split()))
dp = [1]*N

for i in range(1, N):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


# O(nlogn) 풀이
## 이분 탐색을 통해서 O(n) 이었던 나보다 작은 수 탐색과정을 O(logn) 으로 줄이는 방식
## 이분 탐색을 위해 오름차순 정렬되는 배열을 만들어가면서 진행
## 이 때, 매 수를 탐색한 이후에 그 수보다 한단계 큰 수(아래 코드에서는 이분 탐색의 return 값)를 탐색한 수로 갱신해준다.
### 이는 최대한 작은 수를 배열에 정리하여 유지하기 위함
def bin_search(k):
    left = 0
    right = len(order)-1
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
order = [0]

for i in range(1, N+1):
    idx = bin_search(numbers[i])
    if idx >= len(order):
        order.append(numbers[i])
    else:
        order[idx] = numbers[i]
    dp[i] = idx

print(max(dp))