# https://www.acmicpc.net/problem/10813

n, m = map(int, input().split())
bucket = [str(i + 1) for i in range(n)]
for _ in range(m):
    i, j = map(lambda x: int(x) - 1, input().split())
    bucket[i], bucket[j] = bucket[j], bucket[i]
print(" ".join(bucket))
