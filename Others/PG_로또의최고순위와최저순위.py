def solution(lottos, win_nums):
    rank = [6, 5, 4, 3, 2]
    answer = []
    chk = zeros = 0
    for num in lottos:
        if num in win_nums:
            chk += 1
            continue
        if num == 0:
            zeros += 1

    for i in range(len(rank)):
        if rank[i] == (zeros + chk):
            answer.append(i + 1)
        if rank[i] == chk:
            answer.append(i + 1)
    if len(answer) == 1:
        answer.append(6)
    if len(answer) == 0:
        answer = [6, 6]

    return answer