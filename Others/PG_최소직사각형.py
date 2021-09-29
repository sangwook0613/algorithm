# 프로그래머스 최소직사각형

def solution(sizes):
    answer = 0
    first = []
    second = []
    for a, b in sizes:
        first.append(a)
        second.append(b)

    if max(first) > max(second):
        sizes.sort()
    else:
        sizes.sort(key=lambda x: x[1])
    print(sizes)
    print(first, second)

    for i in range(len(sizes)):
        if sizes[i][0] < max(second) and sizes[i][1] < max(first):
            first[i], second[i] = second[i], first[i]
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    print(sizes)
    print(first, second)

    return answer