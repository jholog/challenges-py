# https://www.acmicpc.net/problem/18353

n = int(input())
arr = list(map(int, input().split()))[::-1]
dp = [1] * len(arr)

for i in range(1, len(arr)):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
