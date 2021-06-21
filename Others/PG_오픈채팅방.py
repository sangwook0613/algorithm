def solution(record):
    answer = []
    result = []

    # dict 을 활용해서 아이디의 닉네임을 관리하는 것이 핵심인 문제!
    nicknames = {}

    for r in record:
        order = r.split()
        if order[0] == 'Enter':
            idname = order[1]
            nick = order[2]
            nicknames[idname] = nick
            result.append([order[1], '님이 들어왔습니다.'])
        elif order[0] == 'Leave':
            result.append([order[1], '님이 나갔습니다.'])
        else:
            idname = order[1]
            nick = order[2]
            nicknames[idname] = nick

    for res in result:
        answer.append(nicknames[res[0]] + res[1])

    return answer