# 백준 4358 생태학
## dictionary 자료 구조를 사용해서 해결
## 입력 받을 때 EOFError를 사용해서 처리
trees = {}
count = 0
while True:
    try:
        name = input()
        trees[name] = trees[name] + 1 if trees.get(name) else 1
        count += 1
    except EOFError:
        break

result = sorted(trees.items())
for tree, num in result:
    print(tree, format(round((num / count)*100, 4), '.4f'))