# 백준 1942 디지털시계
## 반복문을 통해서 푸는 간단한 문제
for _ in range(3):
    start, end = input().split()
    start_time = list(map(int, start.split(':')))
    end_time = list(map(int, end.split(':')))
    curr_time = start_time[:]
    ans = 0
    while True:
        num = curr_time[0]*10000 + curr_time[1]*100 + curr_time[2]
        if num % 3 == 0:
            ans += 1

        # 종료 조건
        if curr_time == end_time:
            break

        curr_time[2] += 1
        if curr_time[2] > 59:
            curr_time[2] = 0
            curr_time[1] += 1
        if curr_time[1] > 59:
            curr_time[1] = 0
            curr_time[0] += 1
        if curr_time[0] > 23:
            curr_time[0] = 0

    print(ans)