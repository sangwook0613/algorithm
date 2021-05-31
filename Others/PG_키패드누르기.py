def chk_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def solution(numbers, hand):
    answer = ''
    board = []
    for i in range(4):
        board.append([i * 3 + 1, i * 3 + 2, i * 3 + 3])
    left_finger = [3, 0]
    right_finger = [3, 2]

    idx = 0
    while idx < len(numbers):
        if numbers[idx] % 3 == 0 and numbers[idx] != 0:
            answer += 'R'
            right_finger = [(numbers[idx] // 3) - 1, 2]
        elif numbers[idx] % 3 == 1:
            answer += 'L'
            left_finger = [(numbers[idx] // 3), 0]
        else:
            num_point = []
            if numbers[idx] == 0:
                num_point = [3, 1]
            else:
                num_point = [(numbers[idx] // 3), 1]

            if chk_dist(num_point, left_finger) > chk_dist(num_point, right_finger):
                answer += 'R'
                right_finger = num_point
            elif chk_dist(num_point, left_finger) < chk_dist(num_point, right_finger):
                answer += 'L'
                left_finger = num_point
            else:
                if hand == 'left':
                    answer += 'L'
                    left_finger = num_point
                else:
                    answer += 'R'
                    right_finger = num_point
        idx += 1

    return answer