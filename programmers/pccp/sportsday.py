from itertools import permutations


def solution(ability):
    global answer
    answer = 0

    students = [i for i in range(len(ability))]

    p = permutations(students, len(ability[0]))
    for s in p:
        score = 0
        for i in range(len(s)):
            score += ability[s[i]][i]
        answer = score if answer < score else answer

    visited = [0] * len(ability)

    def dfs(i, score):
        global answer
        if i == len(ability[0]):
            if answer < score:
                answer = score
            return

        for s in range(len(ability)):
            if visited[s]:
                continue
            visited[s] = 1
            score += ability[s][i]
            dfs(i + 1, score)
            score -= ability[s][i]
            visited[s] = 0

    dfs(0, 0)

    return answer


if __name__ == '__main__':
    # 순열/dfs, PCCP 모의고사 1회, 체육대회 문제
    # https://school.programmers.co.kr/learn/courses/15008/lessons/121684
    print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
    print(solution([[20, 30], [30, 20], [20, 30]]))
