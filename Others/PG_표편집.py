# 프로그래머스 표 편집
## 정확성만 통과하는 코드
## test 를 다시 업데이트 과정에서 for문이 추가적으로 진행되기 때문에 효율성 시간초과
def solution(n, k, cmd):
    answer = ''
    chk = [[i, 1] for i in range(n)]
    test = [i for i in range(n)]
    stack = []
    curr = k
    for c in cmd:
        temp = c.split(' ')
        if len(temp) > 1:
            if temp[0] == 'D':
                curr += int(temp[1])
            else:
                curr -= int(temp[1])
        else:
            if temp[0] == 'C':
                chk[test[curr]][1] = -1
                stack.append(test.pop(curr))
                if curr == len(test):
                    curr = len(test)-1
            else:
                z = stack.pop()
                if z <= test[curr]:
                    curr += 1
                chk[z][1] = 1
                test = []
                for a in range(n):
                    if chk[a][1] > 0:
                        test.append(a)

    for a in range(n):
        if chk[a][1] > 0:
            answer += 'O'
        else:
            answer += 'X'
    return answer


# 정확성, 효율성 모두 통과하는 코드
## 위로 올라갈 때와 아래로 내려갈때의 인덱스를 잘 다뤄어야 하는 풀이
## 한번 더 읽고 정리할 필요가 있다!
def solution(n, k, cmd):
    answer = ''
    up = [i for i in range(-1, n - 1)]
    down = [i for i in range(1, n)] + [-1]
    numbers = [1] * n
    stack = []

    for c in cmd:
        temp = c.split()
        if len(temp) > 1:
            if temp[0] == 'U':
                for _ in range(int(temp[1])):
                    k = up[k]
            else:
                for _ in range(int(temp[1])):
                    k = down[k]
        else:
            if temp[0] == 'C':
                numbers[k] = 0
                stack.append(k)
                if up[k] != -1:
                    down[up[k]] = down[k]
                if down[k] != -1:
                    up[down[k]] = up[k]
                k = down[k] if down[k] != -1 else up[k]
            else:
                z = stack.pop()
                numbers[z] = 1
                if up[z] != -1:
                    down[up[z]] = z
                if down[z] != -1:
                    up[down[z]] = z

    return ''.join([('O' if i else 'X') for i in numbers])