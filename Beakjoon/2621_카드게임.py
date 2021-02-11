colors = []
numbers = []
counts = [0] * 10
max_num = 0
same_color_count = 0
check_color = ''
for i in range(5):
    color, num = map(str, input().split())
    colors += [color]
    numbers += [int(num)]
    counts[int(num)] += 1
    # 최댓값 구하기
    if int(num) > max_num:
        max_num = int(num)
    # 겹치는 색 count
    if i == 0:
        check_color = color
        same_color_count = 1
    else:
        if color == check_color:
            same_color_count += 1
        else:
            same_color_count = 0

# 버블 정렬
for i in range(1, 5):
    for j in range(5-i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# 색이 모두 같은 경우(600, 900)
if same_color_count == 5:
    straight_count1 = 1
    start_num1 = numbers[0]
    for a in range(1, len(numbers)):
        if numbers[a] == start_num1+1:
            start_num1 += 1
            straight_count1 += 1
        else:
            break
    if straight_count1 == 5:
        print(900 + max_num)
    else:
        print(600 + max_num)
else:
    # 숫자만 연속적인 경우(500)
    straight_count2 = 1
    start_num2 = numbers[0]
    for a in range(1, len(numbers)):
        if numbers[a] == start_num2+1:
            start_num2 += 1
            straight_count2 += 1
        else:
            break
    if straight_count2 == 5:
        print(500 + max_num)
    else:
        # 겹치는 숫자의 수에 따른 경우
        many_num = [0, 0]
        for i in range(1, len(counts)):
            if counts[i] > many_num[0]:
                many_num[0] = counts[i]
                many_num[1] = i

        if many_num[0] == 4:
            print(800 + many_num[1])
        elif many_num[0] == 3:
            second_many_num = [0, 0]
            for i in range(1, len(counts)):
                if counts[i] > second_many_num[0] and counts[i] != 3:
                    second_many_num[0] = counts[i]
                    second_many_num[1] = i
            if second_many_num[0] == 2:
                print(many_num[1]*10 + second_many_num[1] + 700)
            else:
                print(400 + many_num[1])
        elif many_num[0] == 2:
            second_many_num = [0, 0]
            for i in range(1, len(counts)):
                if counts[i] > second_many_num[0] and i != many_num[1]:
                    second_many_num[0] = counts[i]
                    second_many_num[1] = i
            if second_many_num[0] == 2:
                if many_num[0] > second_many_num[0]:
                    print(many_num[1]*10 + second_many_num[1] + 300)
                else:
                    print(second_many_num[1] * 10 + many_num[1] + 300)
            else:
                print(200 + many_num[1])
        else:
            print(100 + max_num)