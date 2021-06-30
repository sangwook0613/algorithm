# 2018 KAKAO BLIND RECRUITMENT
## 파이썬의 메소드들을 활용할 줄 알면 쉽게 풀리는 문제


def solution(files):
    answer = []
    sep_files = []
    files_len = len(files)
    for i in range(files_len):
        chk_int = 0
        temp = [i]
        head = ''
        number = ''
        for s in files[i]:
            if chk_int and not s.isdigit():
                break
            if s.isdigit():
                if chk_int == 0:
                    temp.append(head.lower())
                chk_int = 1
                number += s
            else:
                head += s
        temp.append(int(number))
        sep_files += [temp]

    sep_files.sort(key=lambda x: (x[1], x[2], x[0]))
    for i in range(files_len):
        answer.append(files[sep_files[i][0]])

    return answer