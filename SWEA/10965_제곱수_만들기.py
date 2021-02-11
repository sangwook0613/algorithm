T = int(input())

for t in range(1, T+1):
    num = int(input())
    for i in range(1, num+1):
        temp = num * i
        ans = 0
        for j in range(1, temp + 1):
            if temp % j == 0 and temp // j == j:
                ans = i
                break
        if ans > 0:
            print('#%d %d' % (t, ans))
            break