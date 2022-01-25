# 백준 12757 전설의 JBNU
## 이분 탐색을 통해서 인접한 key를 찾는 계산량을 줄여야 풀 수 있는 문제
## 이분 탐색에서 나온 가장 인접한 인덱스를 포함 좌우 인덱스까지 고려해서 key를 찾아낸다
import sys
input = sys.stdin.readline

def binary_search(left, right, num, k):
    # 이분 탐색
    while left <= right:
        mid = (left + right) // 2
        if num <= keys[mid]:
            right = mid - 1
        else:
            left = mid + 1

    result = []
    min_diff = 100000
    # 범위 내에 있는 key 의 수 판단하기
    for i in range(right-1, right+2):
        if i >= len(keys):
            break
        if num - k <= keys[i] <= num + k:
            diff = abs(keys[i] - num)
            if min_diff == diff:
                if result[0] != keys[i]:
                    result.append(keys[i])
            elif min_diff > diff:
                min_diff = diff
                result = [keys[i]]

    if len(result) >= 2 or len(result) == 0:
        return False, result
    return True, result


N, M, K = map(int, input().split())
db = dict()
keys = []
for _ in range(N):
    a, b = map(int, input().split())
    db[a] = b
    keys.append(a)
keys.sort()

for _ in range(M):
    command = list(map(int, input().split()))
    # 1번 경우 - 데이터 추가
    if command[0] == 1:
        db[command[1]] = command[2]
        keys.append(command[1])
        keys.sort()
    # 2번 경우 - 데이터 변경
    elif command[0] == 2:
        chk, search_list = binary_search(0, len(keys)-1, command[1], K)
        if chk:
            db[search_list[0]] = command[2]
    # 3번 경우 - 데이터 출력
    else:
        chk, search_list = binary_search(0, len(keys)-1, command[1], K)
        if chk:
            print(db[search_list[0]])
        else:
            if len(search_list) > 1:
                print('?')
            else:
                print(-1)