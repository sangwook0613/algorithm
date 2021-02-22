T = int(input())

for t in range(1, T+1):
    memory = input()
    bit1 = []
    for i in range(len(memory)):
        bit1 += [memory[i]]
    start = ['0'] * len(memory)

    cnt = 0
    for i in range(len(memory)):
        if memory[i] != start[i]:
            cnt += 1
            for j in range(i+1, len(memory)):
                if int(start[j]):
                    start[j] = '0'
                else:
                    start[j] = '1'

    print('#%d %d' % (t, cnt))