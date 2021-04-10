def get_course(idx, dishes, order, course_num, course_set):
    if len(dishes) == course_num:
        course_set.add(''.join(dishes))
        return

    for k in range(idx, len(order)):
        dishes.append(order[k])
        get_course(k + 1, dishes, order, course_num, course_set)
        dishes.pop()


def solution(orders, course):
    course_set = set()
    for order in orders:
        order = ''.join(sorted(order))
        for num in course:
            get_course(0, [], order, num, course_set)

    order_by_num = [[] for _ in range(len(course))]
    course_by_num = []
    for k in course:
        temp = []
        for i in course_set:
            if len(i) == k:
                temp.append(i)
        if len(temp) < 2:
            temp = []
        course_by_num.append(temp)

    for a in range(len(course)):
        for c_set in course_by_num[a]:
            total = 0
            for order in orders:
                cnt = 0
                for dish in c_set:
                    if dish in order:
                        cnt += 1
                if cnt == len(c_set):
                    total += 1
            order_by_num[a].append(total)

    answer = []
    for i in range(len(course)):
        if len(order_by_num[i]) > 0:
            max_order = max(order_by_num[i])
            if max_order == 1:
                continue
            for j in range(len(order_by_num[i])):
                if order_by_num[i][j] == max_order:
                    answer.append(course_by_num[i][j])
    answer.sort()

    return answer