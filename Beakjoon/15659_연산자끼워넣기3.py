# 백준 15659 연산자 끼워넣기 (3)
## 재귀를 활용해 완전탐색하여 푼 문제
## 배열에 lambda를 담아서 계산
## eval 사용하지 않음
cal = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x // y]

def get_ans(num, oper):
    new_num = []
    new_oper = []
    curr_num = num[0]
    idx = 0
    while idx < len(oper):
        if oper[idx] >= 2:
            curr_num = cal[oper[idx]](curr_num, num[idx+1])
            idx += 1
            continue
        else:
            new_num.append(curr_num)
            new_oper.append(oper[idx])
        idx += 1
        curr_num = num[idx]
    new_num.append(curr_num)

    result = new_num[0]
    for i in range(len(new_oper)):
        result = cal[new_oper[i]](result, new_num[i+1])
    return result


def solve(cnt, arr):
    if cnt == N-1:
        global max_ans, min_ans
        # 계산
        ans = get_ans(numbers, arr)
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
        return
    for i in range(4):
        if operator[i]:
            arr.append(i)
            operator[i] -= 1
            solve(cnt + 1, arr)
            arr.pop()
            operator[i] += 1


N = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_ans = -1000000000
min_ans = 1000000000

solve(0, [])
print(max_ans)
print(min_ans)