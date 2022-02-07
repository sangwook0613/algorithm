# 백준 1080 행렬
## 그리디하게 하나씩 처리하면서 풀어나간 문제
## (0,0) 에서 (N-1,M-1) 까지 순차적으로 보면서 target 값과 맞다면 그대로 두고
## 바꿔야 한다면 바꾼 후 넘어가는 식으로 처리
def solve(cnt):
    for i in range(N):
        for j in range(M):
            if board[i][j] != target[i][j]:
                # 바꿀 수 없다면 -1 을 return
                if i + 2 < N and j + 2 < M:
                    for a in range(3):
                        for b in range(3):
                            board[i + a][j + b] = '0' if board[i + a][j + b] == '1' else '1'
                    cnt += 1
                else:
                    return -1

    return cnt


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
target = [list(input()) for _ in range(N)]
print(solve(0))