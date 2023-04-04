# https://www.acmicpc.net/problem/2444

n = int(input()) * 2 - 1
alist = list(range(1, n + 1, 2))
for i in alist:
    print(("*" * i).center(n).rstrip())
del alist[-1]
for i in alist[::-1]:
    print(("*" * i).center(n).rstrip())
