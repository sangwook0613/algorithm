def solution(enroll, referral, seller, amount):
    answer = {}
    parent = {}

    for name in enroll:
        answer[name] = 0
        parent[name] = name

    for i in range(len(referral)):
        parent[enroll[i]] = referral[i]

    for k in range(len(seller)):
        name = seller[k]
        answer[name] += amount[k] * 90
        money = amount[k] * 10
        while parent[name] != '-':
            name = parent[name]
            answer[name] += money - int(money / 10)
            money = int(money / 10)

    ans = []
    for idx, value in answer.items():
        ans.append(value)
    return ans