import sys

### Stack 클래스 생성해서 풀기 ###
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def empty(self):
        if len(self.stack) == 0:
            return 1
        return 0

    def top(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)


N = int(sys.stdin.readline())
s = Stack()

for i in range(N):
    order = list(map(str, sys.stdin.readline().split()))
    if order[0] == 'push':
        s.push(int(order[1]))
    elif order[0] == 'pop':
        print(s.pop())
    elif order[0] == 'top':
        print(s.top())
    elif order[0] == 'size':
        print(s.size())
    else:
        print(s.empty())


### list로 풀기 ###
for i in range(N):
    order = list(map(str, sys.stdin.readline().split()))
    if order[0] == 'push':
        stack += [int(order[1])]
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
            continue
        print(stack[len(stack)-1])
        stack = stack[:len(stack)-1]
    elif order[0] == 'top':
        if len(stack) == 0:
            print(-1)
            continue
        print(stack[len(stack)-1])
    elif order[0] == 'size':
        print(len(stack))
    else:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
