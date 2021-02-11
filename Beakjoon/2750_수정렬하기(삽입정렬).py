N = int(input())
numbers = [0] * N
for i in range(N):
    numbers[i] = int(input())

for i in range(N-1):
    j = i
    while numbers[j] > numbers[j+1]:
        if j < 0:
            break
        temp = numbers[j+1]
        numbers[j+1] = numbers[j]
        numbers[j] = temp
        j -= 1

for num in range(N):
    print(numbers[num])