def solution(N, stages):
    answer = []
    trys = [[0, 0] for _ in range(N + 1)]
    for s in stages:
        if s > N:
            trys[N][0] += 1
            trys[N][1] += 1
            continue
        trys[s][0] += 1

    for i in range(N, 1, -1):
        trys[i - 1][1] = trys[i][0]
        trys[i - 1][0] += trys[i][0]

    success = []
    for i, x in enumerate(trys):
        if i == 0:
            continue
        if x[0] == 0:
            success.append((i, 1))
        else:
            success.append((i, x[1] / x[0]))

    success.sort(key=lambda x: x[1])

    for k in success:
        answer.append(k[0])

    return answer