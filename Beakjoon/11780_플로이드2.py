# 백준 11780 플로이드2
## 모든 정점에서 모든 정점으로 가는 최단거리를 구하는 문제이기에 플로이드 와샬 알고리즘 사용
## 플로이드 와샬 알고리즘의 핵심은 i 에서 j 를 가는 루트에서 k 를 거쳐가는 루트를 반영하는 것
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
BIG = 10000000 # 임의의 큰 수
board = [[BIG]*(N+1) for _ in range(N+1)] # 최단거리 값들이 들어갈 n*n 배열
connections = [[[] for _ in range(N+1)] for _ in range(N+1)] # 루드를 기록할 배열
# 입력을 받으면서 n*n 를 최솟값으로 갱신
for _ in range(M):
    a, b, c = map(int, input().split())
    board[a][b] = min(board[a][b], c)

# 입력 받은 값에 대한 루트 초기화 과정
for i in range(N+1):
    for j in range(N+1):
        # 입력을 받은 경우, string 형태로 경로를 만듦 (출력을 편하게 하기 위해)
        if board[i][j] != BIG:
            connections[i][j].append(str(i))
            connections[i][j].append(str(j))
        # 미리 초기화
        if i == j:
            board[i][j] = 0

# 플로이드 와샬 알고리즘의 핵심부분
# i 에서 j 를 가는 과정에서 k 를 거쳐야 하니 가장 바깥 for 문에서 k 값을 갱신
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            # 만약 현재 i 에서 j 로 가는 거리보다 i ~ k ~ j 로 가는 거리가 짧다면 갱신
            if board[i][j] > (board[i][k] + board[k][j]):
                board[i][j] = board[i][k] + board[k][j]
                # 경로도 갱신하는데 이 때, k ~ j 로 가는 경로에서 k 가 중복될 수 있기에 슬라이승 하여 붙인다.
                connections[i][j] = connections[i][k] + connections[k][j][1:]

# 최단 거리 값 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        # 큰 값이 있다면 0으로 출력
        if board[i][j] == BIG:
            print(0, end=' ')
        else:
            print(board[i][j], end=' ')
    print()

# 최단 거리 이동 경로 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        if len(connections[i][j]) == 0:
            print(0)
        else:
            print(len(connections[i][j]), ' '.join(connections[i][j]))