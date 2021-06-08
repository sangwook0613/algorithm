def solution(s):
    answer = []
    start = 0
    temp_num = ''
    tuples = []
    temp_tuple = []
    for i in range(1, len(s) - 1):
        if s[i] == '{':
            start = 1
            continue
        if start:
            if s[i].isdigit():
                temp_num += s[i]
            else:
                if s[i] == ',':
                    temp_tuple.append(int(temp_num))
                    temp_num = ''
                else:
                    if len(temp_num) != 0:
                        temp_tuple.append(int(temp_num))
                        temp_num = ''
                    start = 0
                    tuples.append(temp_tuple)
                    temp_tuple = []

    tuples.sort(key=lambda x: len(x))

    answer.append(tuples[0][0])
    for nums in tuples[1:]:
        for num in nums:
            break_chk = 0
            if num not in answer:
                answer.append(num)
                break

    return answer