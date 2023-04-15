def solution(n):
    d = [0] * (n + 1)
    d[1] = 1

    for i in range(2, n + 1):
        d[i] = d[i - 2] + d[i - 1]

    return d[n]


if __name__ == '__main__':
    # DP 유형, 피보나치 수
    # https://school.programmers.co.kr/learn/courses/30/lessons/12945
    print(solution(int(input())))
