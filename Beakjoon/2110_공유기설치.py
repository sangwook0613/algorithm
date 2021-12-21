# 백준 2110 공유기 설치
N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort() # 이분 탐색을 사용하기 위한 sort
ans = 0
left = 0
right = house[N-1]-house[0]
# 만약 공유기가 2개만 있다면 양 끝 집에 설치하는 것이 max
if C == 2:
    ans = house[N-1]-house[0]
# 그렇지 않다면 이분 탐색을 활용하여 간격을 찾아본다
else:
    # 이분탐색
    while left <= right:
        # 우선 기본적으로 첫 집에 하나는 설치하며 그 기반은 첫번째 집
        # base는 공유기를 설치한 가장 높은 좌표의 집을 가리킴
        base = house[0]
        cnt = 1 # 현재 공유기를 설치하는 집의 수
        mid = (left+right) // 2
        # for문을 돌면서 mid 간격만큼 공유기를 설치했을 시 몇 개의 집(cnt)에 공유기를 설치하는지 파악
        for i in range(N):
            #  해당 i번째 집이 mid 간격만큼 떨어져 있다면 base를 갱신하고 cnt +1
            if house[i] >= base + mid:
                base = house[i]
                cnt += 1
        # 만약 위 for문에서 설치한 공유기의 집이 C개 보다 많거나 같다면 mid 간격을 키운다
        if cnt >= C:
            ans = mid
            left = mid + 1
        # C보다 적다면 mid 간격을 줄인다
        else:
            right = mid - 1

print(ans)