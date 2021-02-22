T = int(input())

for t in range(1, T+1):
    N = int(input())
    words = input().split()

    mid_idx = N // 2
    print('#%d' % t, end=' ')
    if N % 2:
        for i in range(mid_idx):
            print(words[i], words[mid_idx+1 + i], end=' ')
        print(words[mid_idx])
    else:
        for i in range(mid_idx):
            print(words[i], words[mid_idx + i], end=' ')
        print()