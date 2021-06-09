def make_group(N, arr):
    if len(arr) > N:
        return
    if len(arr) >= 2:
        print(arr)
        groups.append(arr)

    for i in range(N):
        if group_chk[i] == 0:
            arr.append(i)
            group_chk[i] = 1
            # print(arr)
            make_group(N, arr)
            arr.pop()
            group_chk[i] = 0


T = int(input())

for t in range(1, T+1):
    N = int(input())
    boxes = []
    min_height = 0
    for _ in range(N):
        temp = sorted(list(map(int, input().split())))
        min_height = max(max(temp), min_height)
        boxes.append(temp)
    print(boxes, min_height)

    groups = []
    group_chk = [0]*N
    temp = []