# 백준 1527 금민수의 개수
## 재귀와 set을 활용해서 풀었다
def setNumbers(cnt, num):
    numbers.add(num)
    if cnt == 0:
        return
    setNumbers(cnt - 1, num * 10 + 4)
    setNumbers(cnt - 1, num * 10 + 7)


a, b = input().split()
numbers = set()
ans = 0

for i in range(len(a), len(b)+1):
    setNumbers(i, 0)

numbers = list(numbers)
numbers.sort(reverse=True)

for num in numbers:
    if num < int(a):
        break
    if int(a) <= num <= int(b):
        ans += 1

print(ans)


## 좋은 풀이 (시간, 메모리 모두 훨씬 적게 사용)
### 위 풀이에서 set을 list로 바꿔서 sorting 다시하고 for문 진행한 것을
### 하나의 함수에 묶어서 단순하게 진행할 수 있다!
### 너무 어렵게만 생각하지 말자아
def gms(num, min, max):
    if num >= min and num <= max:
        global ans
        ans += 1

    if num <= max:
        gms(num * 10 + 4, min, max)
        gms(num * 10 + 7, min, max)