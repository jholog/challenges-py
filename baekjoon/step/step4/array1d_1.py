# https://www.acmicpc.net/problem/10807

n = int(input())
arr = list(map(int, input().split()))
assert len(arr) == n
print(arr.count(int(input())))
