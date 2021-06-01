def solution(expression):
    oper_dict = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
    }

    answer = 0
    exp_split = []
    temp = ''
    for i in range(len(expression)):
        if expression[i] == '+' or expression[i] == '-' or expression[i] == '*':
            exp_split.append(temp)
            temp = ''
            exp_split.append(expression[i])
        else:
            temp += expression[i]
    exp_split.append(temp)

    operator = ['+', '-', '*']
    orders = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

    for order in orders:
        new_exp = exp_split[:]
        for a in order:
            idx = 0
            while idx < len(new_exp):
                if operator[a] == new_exp[idx]:
                    cal = oper_dict[operator[a]](int(new_exp[idx - 1]), int(new_exp[idx + 1]))
                    new_exp = new_exp[:idx - 1] + [cal] + new_exp[idx + 2:]
                else:
                    idx += 1
        answer = max(abs(int(new_exp[0])), answer)

    return answer