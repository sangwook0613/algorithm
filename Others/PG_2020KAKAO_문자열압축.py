def zip_word(num, s):
    idx = 0
    word_list = []
    while True:
        if idx + num > len(s):
            word_list.append(s[idx:])
            break
        else:
            word_list.append(s[idx:idx+num])
            idx += num

    temp = ""
    before = word_list[0]
    cnt = 1
    for k in range(1, len(word_list)):
        curr = word_list[k]
        if before == curr:
            cnt += 1
        else:
            if cnt == 1:
                temp += before
            else:
                temp += str(cnt) + before
            cnt = 1
        before = curr
    temp += before
    return len(temp)


def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        answer = min(answer, zip_word(i, s))

    return answer