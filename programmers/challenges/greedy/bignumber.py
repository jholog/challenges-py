def solution(number, k):
    answer = []
    for n in number:
        if not answer:
            answer.append(n)
            continue
        while answer[-1] < n and k > 0:
            answer.pop()
            k -= 1
            if not answer or k <= 0:
                break
        answer.append(n)

    while k:
        answer.pop()
        k -= 1

    return ''.join(answer)


if __name__ == '__main__':
    # 그리디 서치/스택, 큰 수 만들기 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/42883
    # print(solution("1924", 2))
    # print(solution("1231234", 3))
    # print(solution("4177252841", 4))
    print(solution("654321", 1))
    print(solution("654321", 5))
