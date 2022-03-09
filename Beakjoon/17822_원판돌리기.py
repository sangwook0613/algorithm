# 백준 17822 원판 돌리기
## 구현 문제
## 회전과 인접한 것을 구현하는 것이 핵심
N, M, T = map(int, input().split())
circle = [[0]*M] + [list(map(int, input().split())) for _ in range(N)]
for c in circle:
    print(c)
print()
for _ in range(T):
    x, d, k = map(int, input().split())
    # 시계방향
    if not d:
        for i in range(x, N+1, x):
            circle[i] = circle[i][M-k:] + circle[i][:M-k]
        for c in circle:
            print(c)
    # 반시계방향
    else:
        for i in range(x, N+1, x):
            circle[i] = circle[i][k:] + circle[i][:k]
        for c in circle:
            print(c)

    # 인접한 수 비교하기
    ## BFS 활용
    new_circle = [[0]*M for _ in range(N+1)]
    visited = [[0]*M for _ in range(N+1)]
    q = [(1, 1, 0)] # 행, 열, 지울지 여부
    while q:
        a, b, c = q.pop(0)
        if a > 1 and circle[a][b] == circle[a-1][b]:
            pass
        if a < N-1 and circle[a][b] == circle[a+1][b]:
            pass
        if circle[a][b] == circle[a][b-1]:
            pass
        if circle[a][b] == circle[a][(b+1)%M]:
            pass
    i-1, (i+1)%M

