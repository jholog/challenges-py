# https://www.acmicpc.net/problem/5597

alist = list(range(1, 31))
for _ in range(28):
    i = int(input())
    alist.remove(i)
print(alist[0])
print(alist[1])