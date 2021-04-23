def solution(n, times):
    answer = int(1e18)
    left = 1
    right = max(times) * n

    while left <= right:
        cnt = 0
        mid = (left + right) // 2

        for t in times:
            if cnt > n:
                break
            cnt += mid // t

        if cnt >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer