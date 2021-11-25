# 백준 17298 오큰수
# 스택을 진짜 잘 써먹어야 하는 문제 - 너무 재밌다...
N = int(input())
numbers = list(map(int, input().split()))
stack = [numbers.pop()]
biggest = ['-1']

for i in range(N-2, -1, -1):
    num = numbers.pop()
    while True:
        # stack 안에 있는 값(stack_num)이 나(num)보다 작으면 그 놈을 pop
        if not len(stack):
            stack.append(num)
            biggest.append('-1')
            break
        stack_num = stack.pop()
        # stack 안에 있는 값(stack_num)이 나(num)보다 크다면 그 값(stack_num)을 biggest에 넣고
        # 그 값(stack_num)과 나(num)를 순차적으로 stack에 append
        if num < stack_num:
            stack.append(stack_num)
            stack.append(num)
            biggest.append(str(stack_num))
            break

biggest.reverse()
print(' '.join(biggest))