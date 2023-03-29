# https://www.acmicpc.net/problem/10871

n, x = map(int, input().split())
a = list(filter(lambda o: int(o) < x, input().split()))
print(" ".join(a))