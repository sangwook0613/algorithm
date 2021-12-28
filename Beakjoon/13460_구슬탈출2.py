# 백준 13460 구슬 탈출2
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우

def move_red(d, redball, blueball):
    while True:
        # 구멍인 경우
        if board[redball[0] + d[0]][redball[1] + d[1]] == 'O':
            return True, redball
        # 벽이거나 파란 공인 경우
        if board[redball[0] + d[0]][redball[1] + d[1]] == '#' or (redball[0] + d[0] == blueball[0] and redball[1] + d[1] == blueball[1]):
            return False, redball
        redball[0] += d[0]
        redball[1] += d[1]


def move_blue(d, redball, blueball):
    while True:
        # 구멍인 경우
        if board[blueball[0] + d[0]][blueball[1] + d[1]] == 'O':
            return True, blueball
        # 벽이거나 빨간 공인 경우
        if board[blueball[0] + d[0]][blueball[1] + d[1]] == '#' or (blueball[0] + d[0] == redball[0] and blueball[1] + d[1] == redball[1]):
            return False, blueball
        blueball[0] += d[0]
        blueball[1] += d[1]


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
hole = []
red = []
blue = []
for i in range(1, N-1):
    for j in range(1, M-1):
        if board[i][j] == 'B':
            board[i][j] = '.'
            blue = [i, j]
        if board[i][j] == 'R':
            board[i][j] = '.'
            red = [i, j]
        if board[i][j] == 'O':
            hole = [i, j]

# 10번까지 시도했을때, 구멍으로 못찾거나 구멍으로 두 공이 다 빠지는 경우, -1
# DFS로 처리 4의 10제곱
# stack에는 공들의 좌표와 횟수만 보관
ans = 11
stack = [[red, blue, 0]]
while stack:
    rp, bp, cnt = stack.pop()
    # 가지치기 1
    if cnt > ans or cnt == 10:
        continue
    for rc in dxy:
        # 위로 옮기기
        if rc == [-1, 0]:
            if rp[0] > bp[0]: # 파란 공 먼저 이동
                in_hole, new_bp = move_blue(rc, rp[:], bp[:])
                if in_hole:
                    continue
                in_hole, new_rp = move_red(rc, rp[:], new_bp[:])
                if in_hole:
                    ans = min(ans, cnt+1)
                    continue
                stack.append([new_rp, new_bp, cnt+1])
            else: # 빨간 공 먼저 이동
                in_hole, new_rp = move_red(rc, rp[:], bp[:])
                if in_hole: # 빨간 공 구멍 통과
                    in_hole, new_bp = move_blue(rc, [0, 0], bp[:])
                    if in_hole:  # 파란 공 구멍 통과 - 실패
                        continue
                    else: # 빨간 공만 구멍 통과 - 성공
                        ans = min(ans, cnt + 1)
                        continue
                else: # 빨간 공 통과 X
                    in_hole, new_bp = move_blue(rc, new_rp[:], bp[:])
                    if in_hole: # 파란 공 구멍 통과 - 실패
                        continue
                    stack.append([new_rp, new_bp, cnt+1])
        # 아래로 옮기기
        if rc == [1, 0]:
            if rp[0] < bp[0]: # 파란 공 먼저 이동
                in_hole, new_bp = move_blue(rc, rp[:], bp[:])
                if in_hole:
                    continue
                in_hole, new_rp = move_red(rc, rp[:], new_bp[:])
                if in_hole:
                    ans = min(ans, cnt+1)
                    continue
                stack.append([new_rp, new_bp, cnt+1])
            else: # 빨간 공 먼저 이동
                in_hole, new_rp = move_red(rc, rp[:], bp[:])
                if in_hole: # 빨간 공 구멍 통과
                    in_hole, new_bp = move_blue(rc, [0, 0], bp[:])
                    if in_hole:  # 파란 공 구멍 통과 - 실패
                        continue
                    else: # 빨간 공만 구멍 통과 - 성공
                        ans = min(ans, cnt + 1)
                        continue
                else: # 빨간 공 통과 X
                    in_hole, new_bp = move_blue(rc, new_rp[:], bp[:])
                    if in_hole: # 파란 공 구멍 통과 - 실패
                        continue
                    stack.append([new_rp, new_bp, cnt+1])
        # 왼쪽으로 옮기기
        if rc == [0, -1]:
            if rp[1] > bp[1]: # 파란 공 먼저 이동
                in_hole, new_bp = move_blue(rc, rp[:], bp[:])
                if in_hole:
                    continue
                in_hole, new_rp = move_red(rc, rp[:], new_bp[:])
                if in_hole:
                    ans = min(ans, cnt+1)
                    continue
                stack.append([new_rp, new_bp, cnt+1])
            else: # 빨간 공 먼저 이동
                in_hole, new_rp = move_red(rc, rp[:], bp[:])
                if in_hole: # 빨간 공 구멍 통과
                    in_hole, new_bp = move_blue(rc, [0, 0], bp[:])
                    if in_hole:  # 파란 공 구멍 통과 - 실패
                        continue
                    else: # 빨간 공만 구멍 통과 - 성공
                        ans = min(ans, cnt + 1)
                        continue
                else: # 빨간 공 통과 X
                    in_hole, new_bp = move_blue(rc, new_rp[:], bp[:])
                    if in_hole: # 파란 공 구멍 통과 - 실패
                        continue
                    stack.append([new_rp, new_bp, cnt+1])
        # 오른쪽으로 옮기기
        if rc == [0, 1]:
            if rp[1] < bp[1]: # 파란 공 먼저 이동
                in_hole, new_bp = move_blue(rc, rp[:], bp[:])
                if in_hole:
                    continue
                in_hole, new_rp = move_red(rc, rp[:], new_bp[:])
                if in_hole:
                    ans = min(ans, cnt+1)
                    continue
                stack.append([new_rp, new_bp, cnt+1])
            else: # 빨간 공 먼저 이동
                in_hole, new_rp = move_red(rc, rp[:], bp[:])
                if in_hole: # 빨간 공 구멍 통과
                    in_hole, new_bp = move_blue(rc, [0, 0], bp[:])
                    if in_hole:  # 파란 공 구멍 통과 - 실패
                        continue
                    else: # 빨간 공만 구멍 통과 - 성공
                        ans = min(ans, cnt + 1)
                        continue
                else: # 빨간 공 통과 X
                    in_hole, new_bp = move_blue(rc, new_rp[:], bp[:])
                    if in_hole: # 파란 공 구멍 통과 - 실패
                        continue
                    stack.append([new_rp, new_bp, cnt+1])
                    
print(ans if ans < 11 else -1)