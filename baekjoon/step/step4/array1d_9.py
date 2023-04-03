# https://www.acmicpc.net/problem/10811

n, m = map(int, input().split())
bucket = list(range(1, n + 1))
for _ in range(m):
    i, j = map(int, input().split())
    sub = bucket[i - 1:j]
    sub.reverse()
    bucket[i - 1:j] = sub
print(" ".join(map(str, bucket)))
