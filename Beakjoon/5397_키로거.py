# 백준 5397 키로거
## 2개의 스택을 활용하여 푸는 문제
### 각각 커서의 앞에 있는지 뒤에 있는지를 대변하는 스택
## 단, 계산량을 O(1) 로 유지하기 위해 뒤에 있는 스택은 역순으로 보관하여 처리
N = int(input())
for _ in range(N):
    word = input()
    stack1 = [] # 커서 앞의 배열
    stack2 = [] # 커서 뒤의 배열
    for w in word:
        if w == '<':
            if len(stack1) > 0:
                stack2.append(stack1.pop())
        elif w == '>':
            if len(stack2) > 0:
                stack1.append(stack2.pop())
        elif w == '-':
            if len(stack1) > 0:
                stack1.pop()
        else:
            stack1.append(w)

    stack1.extend(reversed(stack2))
    print(''.join(stack1))