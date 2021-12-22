# 백준 14676 영우는 사기꾼?
## 입력 값이 10만까지 들어오기 때문에 이중 for문으로 진행 시 시간초과
## for문을 하나만 쓰고 처리해야하는 문제
## connections에서 건설 선행조건에 필요한 건물들이 지어졌는지 유무를 for문이 아닌 배열을 활용하여 판단하는 것이 핵심
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
connections = [[] for _ in range(N+1)]
require_building = [0]*(N+1) # 이 배열이 핵심적인 친구
for _ in range(M):
    a, b = map(int, input().split())
    connections[a].append(b) # 선행되는 건물의 번호를 인덱스로 갖고 그 아래 후행 건물 인덱스를 담는다
    require_building[b] += 1
actions = [list(map(int, input().split())) for _ in range(K)]

count_building = [0]*(N+1) # 해당 번호의 건물이 몇개 설치되었는지 count
check_building = [0]*(N+1) # 해당 번호의 건물을 선행설치 건물로 갖고 있는 건물들에 체크
ans = ''
for action, num in actions:
    # 건물을 세우는 경우
    if action == 1:
        # 선행되어야하는 건물들의 수보다 현재 설치된 수가 적은데 설치하려고 한다면 Lier!
        if check_building[num] < require_building[num]:
            ans = 'Lier!'
            break

        count_building[num] += 1
        # 해당 건물을 선행 건물로 요구하는 건물들의 번호에 check
        for i in connections[num]:
            check_building[i] += 1

    # 건물을 파괴하는 경우
    else:
        # 해당 번호의 건물이 없는데 파괴하려고 한다면 Lier!
        if count_building[num] == 0:
            ans = 'Lier!'
            break

        count_building[num] -= 1
        for i in connections[num]:
            check_building[i] -= 1

print(ans if ans != '' else 'King-God-Emperor')

#########################################################
## pypy3 만 통과하는 코드
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
connections = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    connections[b].append(a)
actions = [list(map(int, input().split())) for _ in range(K)]
building = [0]*(N+1)

ans = ''
for action, num in actions:
    # 건물을 세우는 경우
    if action == 1:
        if len(connections[num]) > 0:
            chk = 0
            for t in connections[num]:
                if not building[t]:
                    chk += 1
                    break
            if chk:
                ans = 'Lier!'
                break
        building[num] += 1

    # 건물을 파괴하는 경우
    else:
        if building[num] == 0:
            ans = 'Lier!'
            break
        else:
            building[num] -= 1

print(ans if ans != '' else 'King-God-Emperor')