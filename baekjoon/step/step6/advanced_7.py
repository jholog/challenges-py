# https://www.acmicpc.net/problem/4344

c = int(input())
for _ in range(c):
    n, *scores = map(int, input().split())
    cnt = len(list(filter(lambda x: x > sum(scores) / n, scores)))
    print("{:.3f}%".format(cnt / n * 100))

# 숏코딩 참조
# for i in [*open(0)][1:]:
#     a, *b = map(int, i.split());
#     print(f'{sum(a * j > sum(b) for j in b) / a:.3%}')
