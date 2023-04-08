from itertools import product


def solution(word):
    alist = []
    for i in range(5):
        alist += list(product(['A', 'E', 'I', 'O', 'U'], repeat=i + 1))
    for i in range(len(alist)):
        alist[i] = "".join(alist[i])
    alist.sort()

    return alist.index(word) + 1


if __name__ == '__main__':
    # 완전탐색 순열 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/84512
    print(solution("AAAAE"))
    print(solution("AAAE"))
    print(solution("I"))
    print(solution("EIO"))
