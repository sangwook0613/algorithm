def get_abs(a):
    if a < 0:
        return -a
    return a

def factorial(k):
    if k == 1:
        return 1
    return factorial(k-1) * k

n = int(input())
numbers = list(map(int, input().split()))
check = [0] * n # 사용했는 여부를 체크 하는 리스트
# localMax = 0 # localMax를 담을 변수
globalMax = 0 # globalMax를 담을 변수
new_list = [0] * n # 새롭게 만들어질 리스트
idx = 0
total = factorial(n)

print(factorial(8))

