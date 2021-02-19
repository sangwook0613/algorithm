## 체크 라는 변수를 통해서, 현재 b와 o의 위치를 기억하고 얼마나 이동할 수 있는지 확인하자
# 만약 이동할 수 있는 범위 내라면, 바로 클릭만 cnt한다.

# 한번 이동할 때 업데이트해야되는 정보들 = 해당 color의 위치, cnt / 전체 cnt idx
# 확인해야되는 정보 = 이 color로 오기 전까지 사용한 cnt

# 4 B 2 O 1 O 2 B 4

T = int(input())

for t in range(1, T+1):
    order = input().split()
    idx = 1
    cnt = 0
    b_chk = 1
    o_chk = 1
    b_cnt = 0
    o_cnt = 0
    while idx < len(order):
        if order[idx] == 'B':
            if abs(int(order[idx+1]) - b_chk) > cnt - b_cnt:
                cnt += abs(int(order[idx+1]) - b_chk) - (cnt - b_cnt) + 1
            else:
                cnt += 1
            b_chk = int(order[idx+1])
            b_cnt = cnt
        else:
            if abs(int(order[idx+1]) - o_chk) > cnt - o_cnt:
                cnt += abs(int(order[idx+1]) - o_chk) - (cnt - o_cnt) + 1
            else:
                cnt += 1
            o_chk = int(order[idx+1])
            o_cnt = cnt
        idx += 2

    print('#%d %d' % (t, cnt))

#     if o_chk > b_chk:
#         if int(order[idx + 1]) > (o_chk - b_chk):
#             cnt += abs(int(order[idx + 1]) - b_chk) + 1 - o_cnt
#         else:
#             cnt += 1
#     else:
#         cnt += abs(int(order[idx + 1]) - b_chk) + 1
#     b_chk = int(order[idx + 1])
#     b_cnt = cnt
# else:
#     if b_chk > o_chk:
#         if int(order[idx + 1]) > (b_chk - o_chk):
#             cnt += abs(int(order[idx + 1]) - o_chk) + 1 - b_cnt
#         else:
#             cnt += 1
#     else:
#         cnt += abs(int(order[idx + 1]) - o_chk) + 1
#     o_chk = int(order[idx + 1])
#     o_cnt = cnt
# idx += 2
# print(cnt, [b_chk, b_cnt], [o_chk, o_cnt])
