# 백준 1935 후위 표기식2
# 후위 표기식은 스택을 통해서 계산해 나가는 방법이다!
# 후위 표기식에 대해서 꼭 까먹지 말자!!
caculate = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a / b,
    '*': lambda a, b: a * b,
}

N = int(input())
formula = input()
numbers = [int(input()) for _ in range(N)]
stack = []

for a in formula:
    if ord(a) >= 65:
        stack.append(numbers[ord(a)-ord('A')])
    else:
        x = stack.pop()
        y = stack.pop()
        stack.append(caculate[a](y, x))

print("{:.2f}".format(stack.pop()))