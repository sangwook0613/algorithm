# 백준 11660 구간 합 구하기5
## 빠른 입력으로 무조건 받아야 시간초과가 안나는 문제
## 나머지 방식은 누적합을 구하는 것과 같다
## 삼항연산자를 많이 사용했으나, 좀 더 빠르게 풀고 싶으면 초기에 2차원 배열을 만들 때 인덱스를 하나 늘려서 만들자
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
row_sum = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        row_sum[i][j] = board[i][j] + (row_sum[i][j-1] if j >= 1 else 0)
        top = board[i-1][j] if i >= 1 else 0
        left = row_sum[i][j-1] if j >= 1 else 0
        board[i][j] += top + left

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = board[x2-1][y2-1] + (board[x1-2][y1-2] if x1 >= 2 and y1 >=2 else 0)
    ans -= ((board[x2-1][y1-2] if y1 >= 2 else 0) + (board[x1-2][y2-1] if x1 >= 2 else 0))
    print(ans)