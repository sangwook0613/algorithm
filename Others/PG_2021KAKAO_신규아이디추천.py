def solution(new_id):
    # 1단계 : 소문자로 변환
    new_id = list(new_id.lower())

    # 2단계 : 사용불가 문자 제외
    allowed_chr = [ord('.'), ord('-'), ord('_')]
    for i in range(ord('a'), ord('z') + 1):
        allowed_chr.append(i)
    for i in range(ord('0'), ord('9') + 1):
        allowed_chr.append(i)

    temp = []
    for k in new_id:
        if ord(k) in allowed_chr:
            temp.append(k)
    new_id = temp

    # 3단계 : 마침표 중복 제거
    temp = [new_id[0]]
    idx = 0
    for i in range(1, len(new_id)):
        if new_id[i] == temp[idx] and new_id[i] == '.':
            continue
        temp.append(new_id[i])
        idx += 1
    new_id = temp

    # 4단계 : 마침표가 처음 혹은 끝이면 제거
    if len(new_id) > 0 and new_id[0] == '.':
        new_id.pop(0)
    if len(new_id) > 0 and new_id[len(new_id) - 1] == '.':
        new_id.pop()

    # 5단계 : 빈문자열 처리
    if len(new_id) == 0:
        new_id.append('a')

    # 6단계 : 문자열 길이가 16 이상일 때 처리
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id.pop()

    # 7단계 : 문자열 길이가 2 이하일 때 처리
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id.append(new_id[len(new_id) - 1])

    answer = ''.join(new_id)
    return answer