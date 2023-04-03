# https://www.acmicpc.net/problem/10810

n, m = map(int, input().split())
bucket = [0 for _ in range(n)]  # or [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    bucket[i - 1:j] = [k] * (j - i + 1)
print(" ".join(map(str, bucket)))
