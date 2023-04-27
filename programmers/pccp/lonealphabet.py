from collections import Counter


def solution(s):
    answer = ''

    c = Counter(s)
    for c, n in list(filter(lambda x: x[1] > 1, c.items())):
        l = s.find(c)
        for i in range(n):
            r = s.find(c, l + 1)
            if r != -1 and abs(l - r) > 1:
                answer += c
                break
            l = r

    return ''.join(sorted(answer)) if len(answer) > 0 else "N"


if __name__ == '__main__':
    # PCCP 모의고사 1회, 외톨이 알파벳 문제
    # https://school.programmers.co.kr/learn/courses/15008/lessons/121683
    print(solution("edeaaabbccd"))
    print(solution("eeddee"))
    print(solution("string"))
    print(solution("zbzbz"))
