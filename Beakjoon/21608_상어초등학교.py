# 백준 21608 상어 초등학교
## 구현 문제 하지만 너무 어렵게 접근하려고 시간을 너무 낭비했다.
### 애초에 입력 최대가 20이여서 제곱인 400이 최대이기에 그냥 한번씩 다보면 된다고 생각하고 시작했어야 했다.
## 한번씩 다 보면서 조건에 맞는 분기만 처리하면 되는 문제
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N = int(input())
students = [[] for _ in range(N**2 + 1)]
final = [[0]*(N+1) for _ in range(N+1)]

for _ in range(N**2):
    numbers = list(map(int, input().split()))
    students[numbers[0]] = numbers[1:]
    max_friends = 0 # 주변에 있는 좋아하는 친구의 수
    max_empty = 0 # 주변에 있는 빈칸의 수
    min_row = 30 # 행 값
    min_col = 30 # 열 값
    # 모든 칸을 다 본다.
    for i in range(1, N+1):
        for j in range(1, N+1):
            # 해당 칸이 빈칸인 경우에만 들여다본다
            if not final[i][j]:
                curr_friends = 0  # i,j 에 위치할 때 주변에 있는 좋아하는 친구의 수
                curr_empty = 0 # i,j 에 위치할 때 주변에 있는 빈칸의 수
                # 주변을 확인하는 for문
                for dx, dy in dxy:
                    x = i + dx
                    y = j + dy
                    if 1 <= x <= N and 1 <= y <= N:
                        # 비어있지 않다면, 좋아하는 친구인지 판단
                        if final[x][y]:
                            # 좋아하는 친구라면
                            if final[x][y] in numbers[1:]:
                                curr_friends += 1
                        # 비어있으면 빈칸 수 +1
                        else:
                            curr_empty += 1

                # i, j 를 다 둘러본 결과를 바탕으로 min_row 와 min_col 을 갱신하기 위한 분기과정
                # 좋아하는 친구가 더 많은 빈칸이면 (1번조건)
                if curr_friends > max_friends:
                    max_friends = curr_friends
                    max_empty = curr_empty
                    min_row = i
                    min_col = j
                # 좋아하는 친구의 수가 같다면 (2번조건)
                elif curr_friends == max_friends:
                    # 주변 빈칸의 수를 비교 (2번조건)
                    if curr_empty > max_empty:
                        max_empty = curr_empty
                        min_row = i
                        min_col = j
                    # 주변 빈칸의 수가 같다면 작은 행, 작은 열로 갱신 (3번조건)
                    elif curr_empty == max_empty:
                        if i < min_row:
                            min_row = i
                            min_col = j
                        elif i == min_row:
                            if j < min_col:
                                min_col = j

    final[min_row][min_col] = numbers[0]


ans = 0
for fr in range(1, N+1):
    for fc in range(1, N+1):
        cnt = 0
        for dx, dy in dxy:
            x = fr + dx
            y = fc + dy
            if 1 <= x <= N and 1 <= y <= N and final[x][y] in students[final[fr][fc]]:
                cnt += 1
        ans += 1000 if cnt == 4 else 100 if cnt == 3 else 10 if cnt == 2 else 1 if cnt == 1 else 0

print(ans)