# 백준 6209 제자리 멀리뛰기
## 이전에 풀었던 공유기설치 문제와 유사한 방식의 이분 탐색 문제
## 이분 탐색에서 mid 값을 탐색의 용도가 아닌 다른 의미로 활용하여 풀어야 한다
D, N, M = map(int, input().split())
island = [int(input()) for _ in range(N)] + [D]
island.sort() # 정렬

ans = 0
left = 0
right = D
# 만약 존재하는 돌섬의 수와 제거할 돌섬의 수가 같으면 정답은 D
if N == M:
    ans = D
# 그렇지 않다면 이분탐색을 진행
else:
    left = 0
    right = D
    # 이분 탐색에서 최소거리의 최댓값을 구하는 원리
    ## 이분 탐색을 통해 얻어가는 mid의 값은 현재 위치에서 다음 위치까지의 거리를 가리킴
    ### 즉, mid가 학생들이 점프할 수 있는 거리를 의미
    ## base에서 mid 만큼 간격을 이동한 거리 밖에 다음 돌섬이 있다면, base를 갱신하고 남아있는 돌섬의 수(cnt)를 늘려준다
    ### 즉, 이분 탐색을 통해 돌섬 사이간의 최대 간격을 조절하고, 이 떄 남아있는 돌섬의 수가 적절하다면 ans를 갱신
    #### (여기서 남아있는 돌섬의 수가 적절하다는 것은 제거할 돌섬의 수 만큼 제거하고 난 만큼보다 크거나 같은 경우를 의미)
    while left <= right:
        cnt = 0 # 남아 있는 돌담의 수
        base = 0 # 현재 위치한 돌섬의 값, 초기값은 0 (시작점)
        mid = (left + right) // 2

        # for 문을 진행하면서 현재 위치(base) 에서 mid 간격 밖에 i 번째 돌섬이 위치하는 확인
        for i in range(N+1):
            # i번째 돌섬의 위치가 base + mid 보다 크다면
            # 현재 위치(base) 갱신 및 남아 있는 돌섬의 수 +1
            if island[i] >= base + mid:
                base = island[i]
                cnt += 1

        # 남아 있는 돌섬의 수가 전체 돌섬의 수(N) + 1(마지막 도착지)에서 제거할 돌담의 수(M) 보다 크거나 같으면
        # ans 갱신 및 left 를 올린다
        if cnt >= N+1-M:
            ans = mid
            left = mid + 1
        # 작다면, right를 줄인다
        else:
            right = mid - 1

print(ans)