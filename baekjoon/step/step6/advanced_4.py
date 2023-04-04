# https://www.acmicpc.net/problem/10812

n, m = map(int, input().split())
bucket = list(range(1, n + 1))
for _ in range(m):
    i, j, k = map(int, input().split())
    sub = bucket[i - 1:j]
    k = sub.index(bucket[k - 1])
    bucket[i - 1:j] = sub[k:] + sub[:k]
print(" ".join(map(str, bucket)))