def get_prime_num(b):
    numbers = [1] * (b+1)
    numbers[0] = 0
    numbers[1] = 0
    idx = 1
    num = 2
    while num < b:
        if num*idx >= b:
            num += 1
            idx = 1
        if numbers[num*idx]:
            if idx == 1:
                idx += 1
                continue
            numbers[num * idx] = 0
        idx += 1

    prime_num = []
    for i in range(2, len(numbers)):
        if numbers[i]:
            prime_num += [i]

    return numbers, prime_num


T = int(input())

num_list = []
for t in range(T):
    num_list += [int(input())]

total, only = get_prime_num(max(num_list))

for t in range(T):
    a = 0
    ans = 0
    while only[a] <= num_list[t] // 2:
        if total[num_list[t]-only[a]]:
            ans += 1
        a += 1
    print(ans)