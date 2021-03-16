dict16 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
          '4': '0100', '5': '0101', '6': '0110', '7': '0111',
          '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
          'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
          }


T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    case = input()
    test_case = []
    for c in case:
        test_case += c

    # 시계 방향으로 4번 회전하기
    cnt = N // 4
    all_password = []
    for a in range(cnt):
        for i in range(4):
            temp = ''
            for j in range(cnt):
                temp += test_case[cnt*i + j]
            if temp not in all_password:
                all_password.append(temp)
        last = test_case[N-1]
        for k in range(N-1, 0, -1):
            test_case[k] = test_case[k-1]
        test_case[0] = last

    # 16진수로 변환
    password16 = []
    for password in all_password:
        number = ''
        for p in password:
            number += dict16.get(p)
        password16.append(int(number))

    # 16진수를 숫자로 변환
    ans = []
    for num in password16:
        total = 0
        pow2 = 1
        while num != 0:
            total += pow2 * (num % 10)
            pow2 *= 2
            num //= 10
        ans.append(total)

    ans.sort()
    print('#%d %d' % (t, ans[len(password16)-K]))