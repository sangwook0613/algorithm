def get_points(n):
    result = []
    for x in range(1, n-1):
        for y in range(2, n):
            for d1 in range(1, y):
                for d2 in range(1, n-y+1):
                    if x + d1 + d2 > n:
                        break
                    result += [[x, y, d1, d2]]
    return result


def divide_city(a, b, d1, d2):
    board = [[0]*N for _ in range(N)]
    # 1번 구역
    for i in range(a+d1):
        for j in range(b):
            board[i][j] = 1
    # 2번 구역
    for i in range(a+d2):
        for j in range(b, N):
            board[i][j] = 2
    # 3번 구역
    for i in range(a+d1-1, N):
        for j in range(b-d1+d2-1):
            board[i][j] = 3
    # 4번 구역
    for i in range(a+d2, N):
        for j in range(b-d1+d2-1, N):
            board[i][j] = 4
    # 5번 구역
    for i in range(d1+d2+1):
        for j in range(-(d1-abs(i-d1)), d2+1-abs(i-d2)):
            board[a+i-1][b+j-1] = 5

    return board



N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
points = get_points(N)
ans = 100000
for i in range(len(points)):
    board = divide_city(points[i][0], points[i][1], points[i][2], points[i][3])
    cnt = [0]*5
    for a in range(N):
        for b in range(N):
            cnt[board[a][b]-1] += people[a][b]

    diff = max(cnt) - min(cnt)
    if diff < ans:
        ans = diff

print(ans)

