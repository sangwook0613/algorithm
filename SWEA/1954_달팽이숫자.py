T = int(input())
# 델타 법칙 선언 <우, 하, 좌, 상> 방향으로!
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for t in range(1, T+1):
    N = int(input())
    snail = []
    # 0으로 채운 N*N을 -1로 둘러싼 (N+2)*(N+2) 배열을 만든다.
    for i in range(N+2):
        temp = []
        for j in range(N+2):
            if j == 0 or j == N+1 or i == 0 or i == N+1:
                temp += [-1]
            else:
                temp += [0]
        snail += [temp]

    r = 1
    c = 0
    cnt = 1
    idx = 0
    # (1, 0)에서부터 시작하면서 # 다음 움직일 칸이 0이라면 움직이고
    # 만약 0이 아닌 다른 숫자로 채워져 있다면, 델타법칙의 다음 방향에 따라 움직인다
    # 한번 움직일 때 마다, cnt를 하나씩 키워주며, cnt가 9보타 클 경우 반복문에서 탈출한다.
    while cnt <= N**2:
        # 델타 법칙의 네 방향을 한번 다 돌았다면 다시 처음 부분으로 갈 수 있게 idx를 초기화한다.
        if idx > 3:
            idx = 0
        if snail[r + dx[idx]][c + dy[idx]] == 0:
            snail[r + dx[idx]][c + dy[idx]] = cnt
            cnt += 1
            r += dx[idx]
            c += dy[idx]
        else:
            idx += 1

    print('#%d' % t)
    # N*N 값들만 출력한다.
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(snail[i][j], end=' ')
        print()