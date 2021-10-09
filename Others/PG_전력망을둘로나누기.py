# 프로그래머스 전력망을 둘로 나누기
## 유니온파인드로 풀었는데도 아니다.. 왜??

def find(tower, a):
    while tower[a] != a:
        a = tower[a]
    return a


def union(tower, a, b):
    x = find(tower, a)
    y = find(tower, b)
    if x > y:
        tower[x] = y
    else:
        tower[y] = x


def solution(n, wires):
    answer = 1000
    for i in range(len(wires)):
        tower = [i for i in range(n + 1)]
        for j in range(len(wires)):
            if j == i:
                continue
            union(tower, wires[j][0], wires[j][1])

        num = [[tower[1], 1], [0, 0]]
        for k in range(2, n + 1):
            if tower[k] == num[0][0]:
                num[0][1] += 1
            else:
                num[1][0] = tower[k]
                num[1][1] += 1
        answer = min(answer, abs(num[0][1] - num[1][1]))
    return answer