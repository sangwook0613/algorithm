# 백준 21610 마법사 상어와 비바라기
## 시뮬레이션 문제 (구현 문제)
## 인덱스의 변화에 유의하면서 진행 - 시간이 너무 오래걸렸다. 단축하자
import sys
input = sys.stdin.readline
# 좌 좌상 상 우상 우 우하 하 좌하
dxy = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
bug_dxy = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

# 비 내리기
def rain(arr):
    for r in arr:
        basket[r[0]][r[1]] += 1

# 물복사버그 처리
def water_copy_bug(arr):
    for r1, r2 in arr:
        count = 0
        for dx, dy in bug_dxy:
            n1 = r1 + dx
            n2 = r2 + dy
            if 0 <= n1 < N and 0 <= n2 < N and basket[n1][n2]:
                count += 1
        basket[r1][r2] += count

# 새로운 구름 생성
def make_cloud(arr):
    result = []
    # visited 를 사용하지 않고 in 연산자를 사용할 시 시간초과 발생
    visited = [[0]*N for _ in range(N)]
    for a in arr:
        visited[a[0]][a[1]] = 1
    for i in range(N):
        for j in range(N):
            if basket[i][j] >= 2 and not visited[i][j]:
                result.append([i, j])
                basket[i][j] -= 2
    return result


N, M = map(int, input().split())
basket = [list(map(int, input().split())) for _ in range(N)]
cloud = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]
for i in range(M):
    d, s = map(int, input().split())
    # s 를 N 으로 나눈 나머지만큼 곱해준다.
    move_dxy = [dxy[d-1][0]*(s % N), dxy[d-1][1]*(s % N)]
    # 1번 : 구름 옮기기
    # 음수인 경우 N 을 더해주고 음수가 아니면 N 으로 나눈 나머지를 갖는다.
    for c in range(len(cloud)):
        cloud[c][0] = N + cloud[c][0] + move_dxy[0] if (cloud[c][0] + move_dxy[0]) < 0 else (cloud[c][0] + move_dxy[0]) % N
        cloud[c][1] = N + cloud[c][1] + move_dxy[1] if (cloud[c][1] + move_dxy[1]) < 0 else (cloud[c][1] + move_dxy[1]) % N

    # 2번 : 비내리기
    rain(cloud)

    # 4번 : 물복사버그
    water_copy_bug(cloud)

    # 3번 : 구름 사라지기 & 5번 : 새로운 구름 생성
    cloud = make_cloud(cloud)


ans = 0
for b in basket:
    ans += sum(b)
print(ans)