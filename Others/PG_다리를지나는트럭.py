# 프로그래머스 다리를 지나는 트럭
## 간단한 큐 관련 문제


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_weight = 0
    bridge = []
    cnt = []
    finish = []
    max_num = len(truck_weights)
    while len(finish) < max_num:
        for t in range(len(cnt)):
            cnt[t] += 1
        if len(cnt) > 0 and cnt[0] == bridge_length:
            truck = bridge.pop(0)
            finish.append(truck)
            cnt.pop(0)
            bridge_weight -= truck

        if len(truck_weights) > 0:
            if bridge_weight + truck_weights[0] <= weight:
                temp = truck_weights.pop(0)
                bridge.append(temp)
                cnt.append(0)
                bridge_weight += temp

        time += 1

    return time