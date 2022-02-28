# 백준 21611 마법사 상어와 블리자드
## 구현(시뮬레이션) 문제
## 회전하는 판에는 인덱스만 저장하고 실제 구슬의 값은 하나의 배열에 저장하여 처리
## 비어있는 칸일 때 처리를 잘못하느라 고생함
### 예외처리는 항상 조심하자!
dxy = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
turn = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 좌 하 우 상
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 순서 만들기
order = [[0]*N for _ in range(N)] # 인덱스를 담아둘 N*N 배열
marvel = [0] # 구슬의 값을 담아둘 N*N 길이의 1차원 배열
idx = 0
cnt = 1
point = [N//2, N//2] # 시작점
for i in range(1, N):
    if idx >= 4:
        idx %= 4
    # 첫번째, idx 방향으로 i 번
    for _ in range(i):
        point[0] += turn[idx][0]
        point[1] += turn[idx][1]
        marvel.append(board[point[0]][point[1]])
        order[point[0]][point[1]] = cnt
        cnt += 1
    idx += 1
    # 두번째, idx+1 방향으로 i 번
    for _ in range(i):
        point[0] += turn[idx][0]
        point[1] += turn[idx][1]
        marvel.append(board[point[0]][point[1]])
        order[point[0]][point[1]] = cnt
        cnt += 1
    idx += 1

# 제일 상단 행 채우기
for _ in range(N-1):
    point[0] += turn[0][0]
    point[1] += turn[0][1]
    marvel.append(board[point[0]][point[1]])
    order[point[0]][point[1]] = cnt
    cnt += 1


ans = 0
for _ in range(M):
    D, S = map(int, input().split())
    # 마법 방향에 따라 지우기
    temp = []
    for s in range(1, S+1):
        temp.append(order[N//2 + s*dxy[D][0]][N//2 + s*dxy[D][1]])

    for t in range(len(temp)-1, -1, -1):
        marvel.pop(temp[t])
        # 지워진만큼 바로바로 채우기
        marvel.append(0)

    # 폭발
    explode = []
    num = marvel[1]
    start_idx = 1
    length = 1
    while True:
        # 폭발의 대상이 되는 구슬과 그 인덱스를 explode 배열에 보관
        for i in range(2, N * N):
            # 애먹었던 포인트 1
            ## 만약 빈칸이라면 지금까지 확인한 것을 넣을지 말지 체크하고 break
            if marvel[i] == 0:
                if length >= 4:
                    explode.append((num, start_idx, length))
                break
            if marvel[i] == num:
                length += 1
            else:
                if length >= 4:
                    explode.append((num, start_idx, length))
                num = marvel[i]
                start_idx = i
                length = 1

        if not explode:
            break
        else:
            # 폭팔이 있었다면, 폭팔한 구슬만큼 지운다
            for k in range(len(explode)-1, -1, -1):
                ans += explode[k][0]*explode[k][2]
                del marvel[explode[k][1]:explode[k][1]+explode[k][2]]
                marvel.extend([0]*explode[k][2])
            # 초기화
            explode = []
            num = marvel[1]
            start_idx = 1
            length = 1

    # 그룹으로 묶어서 구슬 늘리기
    new_marvel = [0] # 새 구슬을 담을 배열
    chk_num = marvel[1] # 현재 구슬 번호
    chk_count = 1 # chk_num 의 연속된 수
    # for 문을 진행하면서 바로바로 새 구슬을 new_marvel 에 채운다.
    for i in range(2, N*N):
        # 애먹었던 포인트 2
        ## 빈 칸일 경우, 이전에 봤던 칸이 빈칸인지 아닌지에 따라 채우지말지 결정 후 break
        if len(new_marvel) >= N*N or marvel[i] == 0:
            if chk_num != 0:
                new_marvel.extend([chk_count, chk_num])
            break
        if marvel[i] == chk_num:
            chk_count += 1
        else:
            new_marvel.extend([chk_count, chk_num])
            chk_num = marvel[i]
            chk_count = 1

    # N*N 을 넘어가는 경우 pop
    if len(new_marvel) - N*N >= 0:
        over_num = len(new_marvel) - N*N
        for _ in range(over_num):
            new_marvel.pop()
    # N*N 을 넘어가지 않는 경우 0 으로 채우기
    else:
        less_num = N*N - len(new_marvel)
        for _ in range(less_num):
            new_marvel.append(0)

    marvel = new_marvel

print(ans)