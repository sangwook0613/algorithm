# 백준 20055 컨베이어 벨트 위의 로봇
## 문제에 나온대로 구현하면 되는 문제
## 대신 문제를 꼼꼼하게 읽어보자!
## 초기 풀이 PyPy3 만 돌아감
N, K = map(int, input().split())
belt = list(map(int, input().split()))
is_robot = [0]*2*N
cnt = 0
ans = 0

while cnt < K:
    ans += 1
    cnt = 0

    # 회전시키기
    new_belt = [belt[-1]] + belt[:2*N-1]
    belt = new_belt

    # 로봇도 같이 회전한다.
    temp = [is_robot[-1]] + is_robot[:2*N-1]
    is_robot = temp

    # 로봇이 내리는 위치 도달여부 파악 후 내리기
    if is_robot[N-1]:
        is_robot[N-1] = 0

    # 로봇 이동하기 - 역순으로 확인하기
    for i in range(2*N-1, -1, -1):
        if is_robot[i]:
            if belt[(i+1) % (2*N)] and not is_robot[(i+1) % (2*N)]:
                is_robot[i] -= 1
                is_robot[(i+1) % (2*N)] += 1
                belt[(i+1) % (2*N)] -= 1

    # 로봇이 내리는 위치 도달여부 파악 후 내리기
    if is_robot[N-1]:
        is_robot[N-1] = 0

    # 로봇 올리기
    if belt[0]:
        is_robot[0] = 1
        belt[0] -= 1

    # 내구도 확인하기
    for i in range(2*N):
        if not belt[i]:
            cnt += 1

print(ans)


## 개선 풀이 Python3 에도 돌아감
## while 문 안에서 2N 만큼의 for문을 진행할 시 시간초과
N, K = map(int, input().split())
belt = list(map(int, input().split()))
robot = []
cnt = 0
ans = 0

while cnt < K:
    ans += 1
    cnt = 0

    # 회전시키기
    belt = [belt[-1]] + belt[:2*N-1]

    # 로봇도 같이 회전한다.
    for i in range(len(robot)):
        robot[i] += 1

    # 로봇이 내리는 위치 도달여부 파악 후 내리기
    if N-1 in robot:
        robot.remove(N-1)

    # 로봇 이동하기 - 역순으로 확인하기
    for i in range(len(robot)):
        if belt[(robot[i]+1) % (2*N)] and (robot[i]+1) % (2*N) not in robot:
            belt[(robot[i] + 1) % (2 * N)] -= 1
            robot[i] += 1

    # 로봇이 내리는 위치 도달여부 파악 후 내리기
    if N-1 in robot:
        robot.remove(N-1)

    # 로봇 올리기
    if belt[0]:
        robot.append(0)
        belt[0] -= 1

    # 내구도 확인하기
    ## 이 친구도 for문이 아닌 count 로 구해야함
    ## count() 도 O(n) 으로 알고 있는데 무슨차이인지 모르겠다...
    cnt = belt.count(0)

print(ans)