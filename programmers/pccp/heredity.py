def find(n, p):
    p -= 1
    stack = []
    while n > 1:
        stack.append(p % 4)  # 형제 사이 개체 순서
        n -= 1
        p //= 4  # 부모 세대의 개체 순서

    while stack:
        num = stack.pop()
        if num == 0:
            return "RR"
        if num == 3:
            return "rr"
    return "Rr"


def solution(queries):
    answer = []

    for n, p in queries:
        answer.append(find(n, p))

    return answer


if __name__ == '__main__':
    # 스택, 유전법칙 문제
    # https://school.programmers.co.kr/learn/courses/15008/lessons/121685
    print(solution([[3, 5]]))
    print(solution([[3, 8], [2, 2]]))
    print(solution([[3, 1], [2, 3], [3, 9]]))
    print(solution([[4, 26]]))
