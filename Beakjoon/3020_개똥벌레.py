# 백준 3020 개똥벌레
## 이분 탐색 풀이
## 마주하는 장애물의 개수를 구하는 방식은 이분탐색으로 풀이
## 첫번째 구간이라고 하면, numbers[0] 에서는 1의 인덱스를 찾고
## numbers[1]에서는 H-1의 인덱스를 찾아서 인덱스 기반으로 개수 구하는 방식
def binary_search(k, left, right, arr):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= k:
            right = mid - 1
        else:
            left = mid + 1
    return N//2 - left


N, H = map(int, input().split())
numbers = [[], []]
for i in range(N):
    numbers[i%2].append(int(input()))

numbers[0].sort()
numbers[1].sort()
ans = 200001
cnt = 0
for i in range(1, H+1):
    # 아래에서 찾는 이분 탐색에서 k는 i
    temp = binary_search(i, 0, N//2-1, numbers[1]) + binary_search(H-i+1, 0, N//2-1, numbers[0])
    # 위에서 찾는 이분 탐색에서 k는 H-i+1
    if temp < ans:
        ans = temp
        cnt = 1
    elif temp == ans:
        cnt += 1

print(ans, cnt)


## 누적합 풀이