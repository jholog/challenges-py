# https://www.acmicpc.net/problem/3052

alist = []
for _ in range(10):
    alist.append(int(input()) % 42)
print(len(set(alist)))
