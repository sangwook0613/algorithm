# 백준 5904 Moo 게임
## 분할과 정복을 활용해서 풀어야 하는 문제
N = int(input())
count = [0, 3]
curr = 1
while count[curr] < N:
    count.append(count[curr]*2 + curr + 3)
    curr += 1

curr -= 1
while True:
    # 1. 이전까지의 합 + 1 + k+2 보다 작고 0 보다 크거나 같은지 확인
    if 0 <= N - count[curr] < (1 + curr + 2):
        # 1-1. 차이가 1이면 m을 출력
        if N - count[curr] == 1:
            print('m')
        # 1-2. 차이가 1이 아니면 o를 출력
        else:
            print('o')
        # 끝, 탈출
        break
    # 2. 0보다 작으면, 더 작은 값을 찾기 위해 index 수정
    elif N - count[curr] < 0:
        curr -= 1
    # 3. 이전까지의 합 + 1 + k+2 보다 크다면, N에서 이전까지의 합 + 1 + k+2 을 빼고 다시 진행
    else:
        N -= (count[curr] + 1 + curr + 2)
        curr -= 1