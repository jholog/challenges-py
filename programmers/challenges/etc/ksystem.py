import math


def is_prime(n):
    if n == 1:
        return 0
    # for i in range(2, n):                     # O(N)
    for i in range(2, int(math.sqrt(n)) + 1):   # O(N^1/2)
        if n % i == 0:
            return 0
    return 1


def solution(n, k):
    answer = 0

    s = ""
    while n > 0:  # 진법 변환
        n, mod = divmod(n, k)
        s += str(mod)

    nums = str(s[::-1]).split("0")

    for num in nums:
        if not num:
            continue
        if is_prime(int(num)):
            answer += 1

    return answer


if __name__ == '__main__':
    # 소수 판별/진법 변환, k 진수에서 소수 개수 구하기 문제 lv.2
    # https://school.programmers.co.kr/learn/courses/30/lessons/92335
    print(solution(437674, 3))
    print(solution(110011, 10))
    print(solution(11223123, 3))
