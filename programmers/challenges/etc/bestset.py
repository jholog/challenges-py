def solution(n, s):
    answer = [s // n for _ in range(n)]
    for i in range(s % n):
        answer[i] += 1
    answer.sort()

    if min(answer) <= 0:
        answer = [-1]

    return answer


if __name__ == '__main__':
    # 구현, 최고의 집합 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/12938
    print(solution(2, 9))
    print(solution(2, 1))
    print(solution(2, 8))
    print(solution(2, 1000000))
