# 백준 11729 하노이 탑 이동 순서
N = int(input())

def hanoi(n, from_num, to_num, leftover):
    # n이 홀수이면, 마지막 위치(3)로, 짝수이면, 마지막이 아닌 다른 위치로 이동
    if n == 1:
        print(from_num, to_num)
        return
    hanoi(n-1, from_num, leftover, to_num) # 맨 밑의 원판을 제외한 나머지를 중앙으로 욺기는 재귀
    print(from_num, to_num) # 맨 밑 원판을 마지막 위치에 옮기기
    hanoi(n-1, leftover, to_num, from_num) # 중앙에 쌓아놓은 원판을 마지막 위치에 옮기기

print(pow(2, N) - 1)
hanoi(N, 1, 3, 2)