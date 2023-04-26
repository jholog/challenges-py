import math


def solution(m):
    dp = [[math.inf for _ in range(len(m))] for _ in range(len(m))]

    for i in range(len(dp)):
        dp[i][i] = 0

    for i in range(1, len(dp)):
        for j in range(0, len(dp) - i):
            s = j
            e = j + i
            for k in range(s, e):
                dp[s][e] = min(dp[s][e],
                               dp[s][k] + dp[k + 1][e] + (m[s][0] * m[k][1] * m[e][1]))

    for d in dp:
        print(d)

    return dp[0][- 1]


if __name__ == '__main__':
    # dp, 최적의 행렬 곱셈 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/12942
    print(solution([[5, 3], [3, 10], [10, 6]]))
    print(solution([[5, 3], [3, 10], [10, 6], [6, 8]]))
    print(solution([[20, 1], [1, 30], [30, 10], [10, 10]]))
    print(solution([[5, 3], [3, 10], [10, 6], [6, 8], [8, 5]]))
